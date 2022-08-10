import requests
import json 

def getCreds():
    creds = dict()
    creds['access_token'] = 'add your access token here'#access token
    creds['client_id'] = 'add your client id here'#client id
    creds['client_secret'] = 'add your client secret here'#client secret
    creds['graph_domain'] = 'https://graph.facebook.com/'
    creds['graph_version'] = 'v14.0'
    creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/'
    creds['debug'] = 'no'
    creds['page_id'] = 'add your fb page id ' # users page id
    creds['instagram_account_id'] = 'add your instagram account id' # users instagram account id
    creds['ig_username'] = 'add your instagram username' # ig username

    return creds 

def makeApiCall(url, endpointParams, debug = 'no'):
    data = requests.get(url, endpointParams)

    response = dict()
    response['url'] = url
    response['endpoint_params'] = endpointParams
    response['endpoint_params_pretty'] = json.dumps(endpointParams, indent = 4)
    response['json_data'] = json.loads(data.content)
    response['json_data_pretty'] = json.dumps(response['json_data'], indent = 4)

    if ('yes' == debug):
       displayApiCallData(response)

    return response

def displayApiCallData(response):
    print ("\nURL: ")
    print (response['url'])
    print ("\nEndpoint Params: ")
    print (response['endpoint_params_pretty'])
    print ("\nResponse: ")
    print (response['json_data_pretty'])
