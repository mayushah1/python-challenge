import csv
import os
from collections import defaultdict
from collections import Counter

election_number = ['1', '2']

for election_data in election_number:

    f1 = os.path.join("election_data_" + election_data + ".csv")
    F2 = os.path.join('output', "election_data_" + election_data + ".csv")


    with open(f1,'r') as csvFile:

        csvReader = csv.reader(csvFile, delimiter=',')
        votes = []
        candidates = []
        wins = []
        winPercent = []
        count = []

        next(csvReader, None)
            
        for row in csvReader:

                # Append data from the row
            votes.append(row[2])



    #candidatelist = [set(votes)]
    #print(candidatelist)
    d = {}
    for w in votes:
        if w in d:
            d[w]+=1
        else:
            d[w]=0
    for key, value in d.items():
        candidates.append(key)
        wins.append(value)

    for k in range(len(wins)):
        v = int(wins[k])/int((len(votes)))
        winPercent.append(v)
    #for a,b,c in zip(candidates,winPercent,wins):
        #print(a,b,c)
    
    maxim = max(d,key=d.get)
    print(f1)
    print("-"*40)
    print("Election Results")
    print("-"*40)
    print("Total Votes: " + str(len(votes)))
    print("-"*40)
    for a,b,c in zip(candidates,winPercent,wins):
        print(a,round(b,2)*100,c)
    print("-"*40)
    print("Winner: " + maxim)
    print("-"*80)


    