import random
from collections import Counter

def run_simulations(nSim, nRepeat, nCols, hCols, colors):
    ### Run simulations ###
    sList = []
    for s in range(nSim):
        resList = []

        for r in range(nRepeat):
            ## Run simulation ##
            oneSimRes = [tuple(random.sample(colors, hCols)) for i in range(nCols)]
            
            ## Count matches ##
            countList = Counter(oneSimRes)
            
            ## Store results ##
            resList.append(list(countList.values()))

        sList.append(resList)

    ### Init res dicts ###
    exactResDict = {i:[] for i in range(2,nCols+1)}
    exactResDict.update({0:[]})
    atLeastResDict = {i:[] for i in range(2,nCols+1)}

    ### Fill res dicts ###
    for sVals in sList:
        exactResDict[0].append(sum([len(i) == 5 for i in sVals]) / nRepeat)

        for k in list(exactResDict.keys())[:-1]:
            exactResDict[k].append(sum([True if sum([k == j for j in i]) == 1 else 0 for i in sVals]) / nRepeat)

        for l in atLeastResDict.keys():
            atLeastResDict[l].append(sum([max(i) >= l for i in sVals]) / nRepeat)

    return exactResDict, atLeastResDict