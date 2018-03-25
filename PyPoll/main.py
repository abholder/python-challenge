# PyPoll

print (""" I know this isn't going to work. I cannot even figure out the 2nd step just trying to calculate the totals. I spent the past week watching class videos and studying online sites like ThinkLikeAComputerScientist.com. I wrote out a flow chart with pencil/paper Thursday night. I worked on the code for about 5 hours or so Friday. Then all afternoon/evening on Saturday. I'm not sure what I'm missing but I'll continue to work on these assignments until I figure them out. Any insight you could provide would be appreciated. ---Aaron """ )

# import modules
import os
import csv

# get first file
csvpath = os.path.join('/Users/aaronholder/Desktop/UKED201802DATA5-Class-Repository-DATA-master-672eee651885c9eb9b3f52c0fa7d3912e197cf31/03-Python/Homework/PyPoll/raw_data', 'election_data_1.csv')

# variables
election_results = []
candidates = []
counties = []
voter_ids = []



# read first file
with open(csvpath, 'r') as csvfile:

    # test import
    # print(csvfile)
    # lines=csvfile.read()
    # print(lines)


    # read data into dictionary
    reader = csv.reader(csvfile)
    election_results = list(reader)
    for row in reader:
        election_results.append(
            {
                "date": row["Date"],
                "monthly_revenue": row["Revenue"]
            }
        )
        
    # total number of months
    print (len(monthly_revenues))
    

   
    
#     # print (float(monthly_revenue))
#     # Turn each "price string" into an actual number
#     for index, monthly_revenue in enumerate(monthly_revenues):
#         monthly_revenue[index] = monthly_revenues
#         monthly_revenues = float(monthly_revenue[index])
#         print (sum(monthly_revenues))
    


#     # total revenue
#     # total_revenue = 0
#     # for x in monthly_revenues:
#     #     monthly_revenue = [(monthly_revenue) for monthly_revenue in monthly_revenues[7:]]
#     #     total_revenue += monthly_revenue
#     # print(monthly_revenue)








# # write updated data to csv file
# csvpath = os.path.join("/Users/aaronholder/Desktop/UKED201802DATA5-Class-Repository-DATA-master-672eee651885c9eb9b3f52c0fa7d3912e197cf31/03-Python/Homework/PyBank/output", "test")
# with open(csvpath, "w") as csvfile:
#     fieldnames = ["date", "monthly_revenue", "total_revenues"]
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(monthly_revenues)