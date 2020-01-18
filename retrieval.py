# Import libraries
import requests
import json


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
