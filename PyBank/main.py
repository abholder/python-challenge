# PyBank

print (""" I know this isn't going to work. I cannot even figure out the 2nd step just trying to calculate the totals. I spent the past week watching class videos and studying online sites like ThinkLikeAComputerScientist.com. I wrote out a flow chart with pencil/paper Thursday night. I worked on the code for about 5 hours or so Friday. Then all afternoon/evening on Saturday. I'm not sure what I'm missing but I'll continue to work on these assignments until I figure them out. Any insight you could provide would be appreciated. ---Aaron """ )


# import modules
import os
import csv

# get first file
csvpath = os.path.join('/Users/aaronholder/Desktop/UKED201802DATA5-Class-Repository-DATA-master-672eee651885c9eb9b3f52c0fa7d3912e197cf31/03-Python/Homework/PyBank/raw_data', 'budget_data_1.csv')

# variables
monthly_revenues = []
total_revenue = 0.00

# read first file


    # test import
    # print(csvfile)
    # lines=csvfile.read()
    # print(lines)


# read data into dictionary
with open(csvpath) as csvfile:
    reader = csv.DictReader(csvfile)
    # monthly_revenues = list(reader)
    for row in reader:
        date = row["Date"]
        monthly_revenue = row["Revenue"]
        monthly_revenues.append
        (
            {
                "date": row["Date"],
                "monthly_revenue": row["Revenue"]
            }
        )
        
    # total number of months
    print (len(monthly_revenues))
    # print (monthly_revenues)

for month in monthly_revenues:
    total_revenue = float(month["monthly_revenue"]) + total_revenue
    
    print(total_revenue)

    # print (float(monthly_revenue))
    # for month in range(1, len(monthly_revenues)):
    #     print(monthly_revenues[month])
    #     monthly_revenues[month][1]=float(monthly_revenues[month][1])
    #     print(monthly_revenues[month])    

    # total revenue
    # total_revenue = 0
    # for x in monthly_revenues:
    #     monthly_revenue = [(monthly_revenue) for monthly_revenue in monthly_revenues[7:]]
    #     total_revenue += monthly_revenue
    # print(monthly_revenue)



# write updated data to csv file
csvpath = os.path.join("/Users/aaronholder/Desktop/UKED201802DATA5-Class-Repository-DATA-master-672eee651885c9eb9b3f52c0fa7d3912e197cf31/python-challenge/PyBank/output", "test")
with open(csvpath, "w") as csvfile:
    fieldnames = ["date", "monthly_revenue", "total_revenues"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(monthly_revenues)