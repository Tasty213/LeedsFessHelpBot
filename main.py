import runner

settings = runner.loadConfig()

try:
    IDs = runner.postRetrieve(settings)
except KeyError:
    runner.longTermTokenRetrieve(settings)
    IDs = runner.postRetrieve(settings)

for i in range(len(IDs)):
    if runner.checkComments(IDs[i], settings) == True:
        print('commenting on ID: ', IDs[i])
        runner.post(IDs[i], settings)
