# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# declare csv file to be read
#csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
csvpath = os.path.join('Resources', 'budget_data.csv')

# initiate variables
months = 0
profit = 0
maxprofitdollar = 0
minprofitdollar = 0

currentmonthprofit = 0
lastmonthprofit = 0
averagemonthtally = 0
averagemonthpl = 0

# open csv file
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Now, read each row of data after the first row
    for row in csvreader:
            # tally of number of months
            months += 1
            
            # running total of profit/loss
            profit += int(row[1])
            
            # set current month profit
            currentmonthprofit = int(row[1])
           
            # compare month to month profits (for max)
            if int(currentmonthprofit - lastmonthprofit) > int(maxprofitdollar):
                maxprofitmonth = row[0]
                maxprofitdollar = int(currentmonthprofit - lastmonthprofit)

            # compare month to month profits (for min)
            if int(currentmonthprofit - lastmonthprofit) < int(minprofitdollar):
                minprofitmonth = row[0]
                minprofitdollar = int(currentmonthprofit - lastmonthprofit)

            if lastmonthprofit != 0:
                #find profit/loss between this month and last month
                averagemonthtally += 1
                averagemonthpl += (currentmonthprofit - lastmonthprofit)
                #print("current month: " + str(currentmonthprofit) + "   last month: " + str(lastmonthprofit))
            
            lastmonthprofit = int(row[1])

    # calculate average monthly profit
    averageprofit = profit / months
    
    print ("average month pl: " + str(averagemonthpl))
    print ("tally :" + str(averagemonthtally))

    averagemonthpl = averagemonthpl / averagemonthtally

    # Display output to screen
    print ("Financial Analysis")
    print ("------------------")
    print ("Total Months: " + str(months))
    print ("Total: ${0:<12,.0f}".format(profit))
    print ("Average change: ${0:<12,.2f}".format(averagemonthpl))
    print ("Greatest Increase in Profits: "  + maxprofitmonth + " ($" + str(maxprofitdollar) + ")")
    print ("Greatest Decrease in Profits: "  + minprofitmonth + " ($" + str(minprofitdollar) + ")")

# Push the output to a text file
with open("financial_analysis.txt", "w") as f:
    print ("Financial Analysis", file=f)
    print ("------------------", file=f)
    print ("Total Months: " + str(months), file=f)
    print ("Total: ${0:<12,.0f}".format(profit), file=f)
    print ("Average change: ${0:<12,.2f}".format(averagemonthpl), file=f)
    print ("Greatest Increase in Profits: "  + maxprofitmonth + " ($" + str(maxprofitdollar) + ")", file=f)
    print ("Greatest Decrease in Profits: "  + minprofitmonth + " ($" + str(minprofitdollar) + ")", file=f)
    