import runner
import retrieval
import commentor

IDs = retrieval.postRetrieve()
print(IDs)

for i in range(len(IDs)):
    if commentor.checkComments(IDs[i]) == True:
        #commentor.post(IDs[i])
        print('commenting')
