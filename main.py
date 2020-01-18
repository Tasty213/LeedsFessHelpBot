# Import the runner library
import runner

# Import the settings dictionary from config.txt
settings = runner.loadConfig()

# Firstly the most recent posts must be pulled from Leedsfess
# They are stored as a list of their facebook IDs
# Attempt to get the IDs using the current settings
try:
    IDs = runner.postRetrieve(settings)
except KeyError:
    # If this fails attempt to acquire a new access token and
    # try again
    runner.longTermTokenRetrieve(settings)
    IDs = runner.postRetrieve(settings)

# Iterate through the list of IDs pulled
for i in range(len(IDs)):
    # Check if they have already been comented on, if they
    # haven't post the message
    if runner.checkComments(IDs[i], settings) == True:
        print('commenting on ID: ', IDs[i])
        runner.post(IDs[i], settings)
