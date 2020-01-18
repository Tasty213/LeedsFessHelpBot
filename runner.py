# Import libraries
import requests
import json

def longTermTokenRetrieve(  ):

    # Constant ID's needed throughout the app
    appId = '457899854959751'
    appSecret = '7ecee5ac6651623bfc286a12e19e9f3d'
    shortTermToken = 'EAAGgdR4ylIcBAFwP6dFYs7kkZAzRRNEZAtYlUOugqGN93fhoo0REOvdUqlZAIARwBBHRNQTWWqP0lbSrJl9VVkb42n34EBPMUJ19ALfIIIf73WdYNPfSsmle7KkLmSaNfJkpIjZBnUaThwsscZA85mUdmGIUyN7yzuX9QGmafDsziJquPuWI6ZBKlvlyNCbEo6agN7qlFDXzQA8wmXrULN'

    # Prepare the url to get the access token with
    urlAccessToken = 'https://graph.facebook.com/v2.10/oauth/access_token?grant_type=fb_exchange_token&client_id=' + appId + '&client_secret=' + appSecret + '&fb_exchange_token=' + shortTermToken

    # Print the URL to be sent to for debugging
    print('URL for Access token request: ', urlAccessToken)

    # Send get request and save returned JSON as a dict
    accessTokenGET = requests.get(urlAccessToken)
    data = accessTokenGET.json()

    # Extract the access token from the dict
    access_token = str(data['access_token'])
    print('Access token received: ', access_token)

def postRetrieve(  ):
    appId = '457899854959751'
    appSecret = '7ecee5ac6651623bfc286a12e19e9f3d'
    longTermToken = 'EAAGgdR4ylIcBABs2UtgNWC3etOFng2Y3AbZCGJgJx6jFV9rFb451osBY6Mr0m01F8rZC6IZCsVlPJLzxlddZC3oFwyHSfffRpcvkaZCoZB0nPuqK6PwalKh8pjPDddNTtQa7bJ1WmURAGJq4M2UK56R297IZAKZCoPFUMWzkEY4CZCjnHj9hZCNhe8'

    # Prepare the GET request for posts
    urlPosts = 'https://graph.facebook.com/v3.3/1625499394249300/posts?access_token=' + longTermToken

    # Takes the returned data and turns it into a dict which has a list in it
    posts = requests.get(urlPosts)
    postsData = posts.json()

    # Calculates the number of items in the list (counting from zero
    postNumber = len(postsData['data'])

    # Create the output list ready to be populated
    messageID = []

    # Open keywords.txt and turn into a list
    with open('keywords.txt') as keywordsSet:
        keywords = keywordsSet.read().splitlines()

    # Iterate through the list and Extract the message IDs ready to be returned
    for i in range(postNumber):
        # Get each individual message and metadata
        messagePack = ((postsData['data'])[i])
        # Separate the message from the metadata
        message = messagePack['message']
        # If any of the keywords in the list loaded from keywords.txt is in the message currently being checked add its messageID to the messageID list
        if any(checker in message for checker in keywords):
            # Add the current ID to the list
            messageID.append(messagePack['id'])

    # Print out a list of messageID's that contain the keywords
    # print(messageID)

    # Return the message ID's to the function caller
    return(messageID)


# Declare module variables
appId = '457899854959751'
appSecret = '7ecee5ac6651623bfc286a12e19e9f3d'
longTermToken = 'EAAGgdR4ylIcBABs2UtgNWC3etOFng2Y3AbZCGJgJx6jFV9rFb451osBY6Mr0m01F8rZC6IZCsVlPJLzxlddZC3oFwyHSfffRpcvkaZCoZB0nPuqK6PwalKh8pjPDddNTtQa7bJ1WmURAGJq4M2UK56R297IZAKZCoPFUMWzkEY4CZCjnHj9hZCNhe8'

# Open the support message that will be commented
with open('support.txt', 'r') as file:
    support = file.read().replace('\n', '')

# This function checks if the support message has already been posted (will return False if it has)
def checkComments( ID ):

    # Prepare the GET request for posts
    urlPosts = 'https://graph.facebook.com/v3.3/' + ID + '/comments?access_token=' + longTermToken

    # Takes the returned data and turns it into a dict which has a list in it
    posts = requests.get(urlPosts)
    postsData = posts.json()

    # Ready the index to store the comments in
    comments = []

    # If no comments have been posted immediately return True
    if bool(postsData['data']) == True:
        # Iterate for the entire length of the postsData list
        for i in range(len(postsData['data'])):
            # Set the current data variable to the meta data of the comment currently being inspected
            data = (postsData['data'])[i]
            # Append the current comment onto the list of comments
            comments.append(data['message'])

        # If the support message is in any of the comments
        if any(checker in support for checker in comments):
            return(False)
        else:
            return(True)
    else:
        return(True)

def post( ID ):
    pass
