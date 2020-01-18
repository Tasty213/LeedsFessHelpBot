# Import libraries
import requests
import json

# Declare module variables
appId = '457899854959751'
appSecret = '7ecee5ac6651623bfc286a12e19e9f3d'
longTermToken = 'EAAGgdR4ylIcBABs2UtgNWC3etOFng2Y3AbZCGJgJx6jFV9rFb451osBY6Mr0m01F8rZC6IZCsVlPJLzxlddZC3oFwyHSfffRpcvkaZCoZB0nPuqK6PwalKh8pjPDddNTtQa7bJ1WmURAGJq4M2UK56R297IZAKZCoPFUMWzkEY4CZCjnHj9hZCNhe8'

# Open the support message that will be commented
with open('support.txt', 'r') as file:
	support = file.read().replace('\n', '')

# This function checks if the support message has already been posted (will return False if it has
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




