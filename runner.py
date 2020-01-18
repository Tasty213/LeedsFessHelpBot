# Import libraries
import requests
import json

def loadConfig():
    """
    loadConfig() imports the settings used by the program from config.txt and
    saves them for later use as a dictionary
    """

    # First load the data from config.txt into a format useable by python
    # The config file object is created with the name keywordsSet
    with open('config.txt') as config:
        # Read in the data from the object, save the result in a list with each
        # line a new entry
        settingsTemp = config.read().splitlines()

    # Remove any lines that from the list that are comments
    # NOTE: a comment is any line that starts with a '#', a '#' partway through
    #       a line will not comment out the rest of the line

    # Create and empty list to hold the indexes of the lines to delete
    toDelete = []

    # Iterate through the list of lines imported
    for i in range(0, len(settingsTemp)):
        # If the current line is a comment the add its index to toDelete
        if settingsTemp[i][0] == '#':
            toPop.append(i)

    # Iterate through the list of elements to delete and delete them
    for i in sorted(toDelete, reverse = True):
        del settingsTemp[i]


    # The settings are stored in a dictionary, the following two entries need
    # to be created now. 'export' is a reference to the export() function which
    # when called exports the current settings. It is called by:
    # settings['export'](settings)
    # NOTE: the export function needs to be passed the settings dictionary
    # The 'keywords' key needs to be added now to that values can be appended
    # to it as it is unknown how many there will be
    settings = {'export': export,
                'keywords': []}

    # Take the current line and find what it is describing then assign it to the
    # relevant key
    for current in settingsTemp:
        if not current.find('appID') == -1:
            settings['appID'] = current[6:]
        elif not current.find('appSecret') == -1:
            settings['appSecret'] = current[10:]
        elif not current.find('shortTermToken') == -1:
            settings['shortTermToken'] = current[15:]
        elif not current.find('longTermToken') == -1:
            settings['longTermToken'] = current[14:]
        elif not current.find('key') == -1:
            settings['keywords'].append(current[4:])
        elif not current.find('support') == -1:
            settings['support'] = current[8:]
        else:
            print('error could not assign this entry to a variable, entry is: ', current)

    # return the settings dictionary
    return settings

def export(settings):
    """
    This functions takes a the settings dictionary and saves it to the
    config.txt file in the correct format to be later imported back into the
    program
    """

    # Make a list of strings for each line of the config.txt file
    # NOTE: theres a \n at the end of each string to ensure each list entry is
    #       saed as a seperate line
    lines = ["# Constant ID's needed throughout the app\n",
            "appID="+settings['appID']+'\n',
            "appSecret="+settings['appSecret']+'\n',
            "shortTermToken="+settings['shortTermToken']+'\n',
            "longTermToken="+settings['longTermToken']+'\n',
            "# Keywords to search for in posts"+'\n']

    # The keywords section needs to be created seperate from the rest to ensure
    # that as many keywords can be specified as needed
    # Iterate across each key in the keywords list
    for key in settings['keywords']:
        # Append a line that contains the key= identifier and the keyword
        lines.append("key="+key+'\n')

    # The support message can now be added
    lines.append("# Support message to post"+'\n')
    lines.append("support="+settings['support']+'\n')

    # Open the config.txt file in overwrite mode
    with open('config.txt', 'w') as config:
        # Write all the lines to the file
        config.writelines(lines)


def longTermTokenRetrieve(settings):

    # Prepare the url to get the access token with
    urlAccessToken = 'https://graph.facebook.com/v5.0/oauth/access_token?grant_type=fb_exchange_token&client_id=' + settings['appID'] + '&client_secret=' + settings['appSecret'] + '&fb_exchange_token=' + settings['shortTermToken']

    # Print the URL to be sent to for debugging
    #print('URL for Access token request: ', urlAccessToken)

    # Send get request and save returned JSON as a dict
    accessTokenGET = requests.get(urlAccessToken)
    data = accessTokenGET.json()

    # Extract the access token from the dict
    access_token = str(data['access_token'])
    #print('Access token received: ', access_token)
    settings['longTermToken'] = access_token
    print(access_token)
    settings['export'](settings)

def postRetrieve(settings):

    # Prepare the GET request for posts
    urlPosts = 'https://graph.facebook.com/v5.0/108772043998503/posts?access_token=' + settings['longTermToken']

    # Takes the returned data and turns it into a dict which has a list in it
    posts = requests.get(urlPosts)
    postsData = posts.json()

    # Calculates the number of items in the list (counting from zero
    postNumber = len(postsData['data'])

    # Create the output list ready to be populated
    messageID = []

    # Iterate through the list and Extract the message IDs ready to be returned
    for i in range(postNumber):
        # Get each individual message and metadata
        messagePack = ((postsData['data'])[i])
        # Separate the message from the metadata
        message = messagePack['message']
        # If any of the keywords in the list loaded from keywords.txt is in the message currently being checked add its messageID to the messageID list
        if any(checker in message for checker in settings['keywords']):
            # Add the current ID to the list
            messageID.append(messagePack['id'])

    # Print out a list of messageID's that contain the keywords
    # print(messageID)

    # Return the message ID's to the function caller
    return(messageID)


# This function checks if the support message has already been posted (will return False if it has)
def checkComments(ID, settings):

    # Prepare the GET request for posts
    urlPosts = 'https://graph.facebook.com/v5.0/' + ID + '/comments?access_token=' + settings['longTermToken']

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
        if any(checker in settings['support'] for checker in comments):
            return(False)
        else:
            return(True)
    else:
        return(True)

def post(ID, settings):
    urlComment = 'https://graph.facebook.com/v5.0/' + ID + '/comments?message=' + settings['support'] + '&access_token=' + settings['longTermToken']
    print(urlComment)
    posts = requests.post(urlComment)
    print(posts)
    postsComment = posts.json()
    print(postsComment)
