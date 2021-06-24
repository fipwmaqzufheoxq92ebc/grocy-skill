
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.batteries_api import BatteriesApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from openapi_client.api.batteries_api import BatteriesApi
from openapi_client.api.calendar_api import CalendarApi
from openapi_client.api.chores_api import ChoresApi
from openapi_client.api.current_user_api import CurrentUserApi
from openapi_client.api.files_api import FilesApi
from openapi_client.api.generic_entity_interactions_api import GenericEntityInteractionsApi
from openapi_client.api.print_api import PrintApi
from openapi_client.api.recipes_api import RecipesApi
from openapi_client.api.stock_api import StockApi
from openapi_client.api.stock_by_barcode_api import StockByBarcodeApi
from openapi_client.api.system_api import SystemApi
from openapi_client.api.tasks_api import TasksApi
from openapi_client.api.user_management_api import UserManagementApi
