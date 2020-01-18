# Import libraries
import requests
import json

# Constant ID's needed throughout the app
appId = '457899854959751'
appSecret = '7ecee5ac6651623bfc286a12e19e9f3d'
shortTermToken = 'EAAGgdR4ylIcBAFwP6dFYs7kkZAzRRNEZAtYlUOugqGN93fhoo0REOvdUqlZAIARwBBHRNQTWWqP0lbSrJl9VVkb42n34EBPMUJ19ALfIIIf73WdYNPfSsmle7KkLmSaNfJkpIjZBnUaThwsscZA85mUdmGIUyN7yzuX9QGmafDsziJquPuWI6ZBKlvlyNCbEo6agN7qlFDXzQA8wmXrULN'

# Prepare the url to get the access token with
urlAccessToken = 'https://graph.facebook.com/v2.10/oauth/access_token?grant_type=fb_exchange_token&client_id=' + appId + '&client_secret=' + appSecret + '&fb_exchange_token=' + shortTermToken


# Print the URL to be sent to for debugging
print('URL for Access token request: ',urlAccessToken)

# Send get request and save returned JSON as a dict
accessTokenGET = requests.get(urlAccessToken)
data = accessTokenGET.json()

# Extract the access token from the dict
access_token = str(data['access_token'])
print('Access token received: ', access_token)
