import csv
import os


budget_number = ['1', '2']

for budget_data in budget_number:

    file = os.path.join("budget_data_" + budget_data + ".csv")
    with open(file,'r') as csv_file1:
        csv_reader = csv.reader(csv_file1, delimiter=',')
        next(csv_reader, None)
    
        dates = []
        revenues = []
        #max_pop = []

        for row in csv_reader:
            date = row[0]
            revenue = row[1]
            dates.append(date)
            revenues.append(revenue)

    revenues = [int(x) for x in revenues]

    for i in range(len(revenues)-1):
        RevChange = [revenues[i+1]-revenues[i]]


    totalchange = sum(RevChange)    
    total = sum(revenues)
    max_val = max(revenues)

    min_val = min(revenues)
    d = {}
    d = dict(zip(dates,revenues))
    maxim = max(d,key=d.get)
    minm = min(d,key=d.get)
    AvgRev = total/len(revenues)
    AvgChange = totalchange/(len(revenues)-1)
    print(file)
    print("Total Months:" + str(len(dates)))
    print('Average change in revenue between months over the entire period: '+ str(AvgChange))  
    print("Total Revenue: $" + str(total))
    print("Average Revenue: $" + str(AvgRev))
    print("Greatest Increase in Revenue: " + maxim +"  " + str(max_val))
    print('Greatest Decrease in Revenue: ' + minm + "  " + str(min_val))
    print("-"*80)


