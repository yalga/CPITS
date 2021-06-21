from __future__ import print_function
import sys, warnings
import deepsecurity
from deepsecurity.rest import ApiException
from pprint import pprint

# Setup
if not sys.warnoptions:
	warnings.simplefilter("ignore")
configuration = deepsecurity.Configuration()
configuration.host = 'https://cloudone.trendmicro.com/api'

# Authentication
configuration.api_key['api-secret-key'] = '655F3434-7C1A-535F-70E0-01F7DACB1715:11363884-300D-473A-101F-868792EDECF4:xcCd+jOHiuwUGgOZqFye7b2KB8BcaLh642rlFDj6nRo='

# Initialization
# Set Any Required Values
api_instance = deepsecurity.ComputersApi(deepsecurity.ApiClient(configuration))
api_version = 'v1'
expand_options = deepsecurity.Expand()
expand_options.add(expand_options.none)
expand = expand_options.list()
overrides = False

try:
	api_response = api_instance.list_computers(api_version, expand=expand, overrides=overrides)
	pprint(api_response)
except ApiException as e:
	print("An exception occurred when calling ComputersApi.list_computers: %s\n" % e)

