import logging
from typing import Optional

from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
from mycroft.skills.context import removes_context
from mycroft.util.parse import extract_number

from .grocy.openapi_client import ApiClient, ApiException, Configuration
from .grocy.openapi_client.api import stock_api, generic_entity_interactions_api


class GrocySkill(MycroftSkill):
    # noinspection PyAttributeOutsideInit
    def initialize(self):
        protocol = self.settings.get('protocol') or 'http'
        host = self.settings.get('host')
        port = self.settings.get('port') or 80
        path = self.settings.get('base_path') or "/"
        if host is None:
            raise Exception('Invalid settings')
        url = f"{protocol}://{host}:{port}{path}api"
        self.log.info('Connecting to grocy at "%s"' % url)
        self._api = ApiClient(
            Configuration(
                host=
                url,
                api_key=self.settings.get('api_key'))
        )
        self._generic = generic_entity_interactions_api.GenericEntityInteractionsApi(self._api)
        self._stock = stock_api.StockApi(self._api)

    def get_product_by_name(self, product_name) -> Optional[dict]:
        """
        Searches for a product with the name `product_name`

        Returns the product (as dict) if it is found, None otherwise.
        :param product_name:
        :return:
        """
        products: list = self._generic.objects_entity_get(entity='products', query=[
            'name~' + product_name
        ])
        self.log.info('%d Products found %r' % (len(products), products))
        if len(products) > 1:
            for p in products:
                if p['name'].lower() == product_name.lower():
                    return p
            else:
                selection = self.ask_selection([p['name'] for p in products])
                try:
                    return next(p for p in products if p['name'] == selection)
                except StopIteration:
                    return None
        if len(products) < 1:
            self.speak_dialog('product-not-found', expect_response=True, data={'product_name': product_name})
            return None
        return products[0]

    @intent_handler('stock-info.intent')
    def stock_info(self, message):
        """
        Get the stock amount of a product
        """
        product_name = message.data.get('product-name')

        try:
            product = self.get_product_by_name(product_name)
            if product is None:
                return
            stock_item = self._stock.stock_products_product_id_get(int(product['id']), _check_return_type=False)
            p = {
                'product': product.get('name'),
                'unit': stock_item['quantity_unit_stock']['name'],
                'amount': stock_item['stock_amount'],

            }
        except ApiException:
            self.speak_dialog('could-not-connect-to-grocy')
        else:
            self.speak_dialog('stock-info', data=p)

    @intent_handler('bought.intent')
    def bought(self, message):
        amount = message.data['amount']
        product_name = message.data['product']
        product = self.get_product_by_name(product_name)
        self._stock.stock_products_product_id_add_post(int(product['id']), {
            "transaction_type": "purchase",
            "amount": float(amount),
        }, _check_return_type=False)
        stock_item = self._stock.stock_products_product_id_get(int(product['id']), _check_return_type=False)
        self.speak_dialog('purchase-product-success', data={
            'product': product.get('name'),
            'unit': stock_item['quantity_unit_stock']['name'],
            'stock_amount': stock_item['stock_amount'],
            'added_amount': float(amount),
            'added_unit': stock_item['default_quantity_unit_purchase']['name']

        })

    # These functions allow "mass-insertion" of purchases.

    @intent_handler('back-from-shopping.intent')
    def back_from_shopping(self, message):
        self.speak_dialog('what-did-you-buy')
        self.set_context('BackFromShoppingContext')

    @intent_handler(IntentBuilder('AddProduct').require('BackFromShoppingContext').require('product').require('amount'))
    def add_product(self, message):
        amount = message.data['amount']
        product_name = message.data['product']
        product = self.get_product_by_name(product_name)
        self._stock.stock_products_product_id_add_post(int(product['id']), {
            "transaction_type": "purchase",
            "amount": float(amount),
        }, _check_return_type=False)
        self._stock.stock_products_product_id_add_post(int(product['id']), {
            "transaction_type": "purchase",
            "amount": float(amount),
        }, _check_return_type=False)
        self.acknowledge()

    @intent_handler(IntentBuilder('FinishShopping').require('BackFromShoppingContext').require('listed-everything'))
    @removes_context('BackFromShoppingContext')
    def finish(self, message):
        self.speak('ok')

    @intent_handler('shopping-list.add.intent')
    def add_to_shopping_list(self, message):
        product = self.get_product_by_name(message.data['product-name'])
        amount = message.data.get('amount', '1')
        amount = extract_number(amount)
        logging.info(
            'Adding %s %s-times to shopping list (%r)' %
            (product['id'], amount, message.data)
        )

        self._stock.stock_shoppinglist_add_product_post({
            "product_id": int(product['id']),
            "list_id": message.data.get('list_id', 1),
            "product_amount": int(amount),

        })
        self.speak_dialog('shopping-list-added', data=product)

    def _get_text_for_shopping_list_item(self, item):
        text = item['note'] or ""
        if item['product_id']:
            product = self._stock.stock_products_product_id_get(
                product_id=int(item['product_id']), _check_return_type=False
            )
            text += f"{item['amount']} {product['default_quantity_unit_purchase']['name']} {product['product']['name']}"
        return text

    def list_to_text(self, iterable):
        separator = self.translate('and')
        return (" " + separator + " ").join(iterable)

    @intent_handler('shopping-list.list.intent')
    def list_shopping_list(self, message):
        shopping_list = self._generic.objects_entity_get('shopping_list')
        self.speak_dialog('shopping-list.list', data={
            'items': self.list_to_text((self._get_text_for_shopping_list_item(item) for item in shopping_list))
        })


def create_skill():
    return GrocySkill()
