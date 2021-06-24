#!/usr/bin/python3
"""
generate the openapi-client for grocy.
"""
import json
import os
import sys

if len(sys.argv) != 2:
    print('You need to pass a url to a running grocy instance as first argument')
    sys.exit(-1)
# Download spec
os.system('wget ' + sys.argv[1] + ' -O grocy.openapi.json')

with open('grocy.openapi.json', 'r') as fp:
    data = fp.read()
    data = data.replace('\\/', '/')

    # Openapi generator has problems with "components/internalSchemas" - just move them to "components/schemas".
    data = data.replace('"#/components/internalSchemas/', '"#/components/schemas/')
    data = json.loads(data)
    data['components']['schemas'].update(**data['components']['internalSchemas'])
    del data['components']['internalSchemas']

with open('grocy.openapi.json', 'w') as fp:
    fp.write(json.dumps(data))

os.system(
    'docker run --user 1000 --rm -v $PWD:/local/ openapitools/openapi-generator-cli generate '
    '-i /local/grocy.openapi.json -g python -o /local/grocy/'
)

os.system(
    'docker run --user 1000 --rm -v $PWD:/local/ debian:10 '
    "sed -i 's/from openapi_client.model.unknownbasetype import UNKNOWNBASETYPE/"
    "UNKNOWN_BASE_TYPE = object\\(\\)/'"
    " /local/grocy/openapi_client/api/generic_entity_interactions_api.py"
)
os.remove('grocy.openapi.json')
