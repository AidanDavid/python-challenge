# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
months = 1
prev_val = 0
curr_val = 0
val_change = []
val_total = 0

# Open and process csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # skip first line
    next(reader)

    # initialize max/min with first val
    line = next(reader)
    max_val, min_val = (line[0], int(line[1])), (line[0], int(line[1]))

    for row in reader:
        # get number of months
        months = months + 1

        # calculate change in profit/loss
        curr_val = int(row[1])
        val_change = prev_val + curr_val

        # calculate total profit/loss
        val_total = val_total + curr_val

        # store the min/max value
        if curr_val > max_val[1]:
            max_val = (row[0], curr_val)
        if curr_val < min_val[1]:
            min_val = (row[0], curr_val)

    output = "Financial Analysis" + "\n----------------------------" + "\nTotal Months: " + str(months) + "\nTotal: $" + str(val_total) + "\nAverage Change: $" + str(round(val_change/months, 2)) + "\nGreatest Increase in Profits: " + max_val[0] + " ($"+ str(max_val[1]) + ")" + "\nGreatest Decrease in Profits: " + min_val[0] + " ($"+ str(min_val[1]) + ")"

    print(output)

# clear text file
#with open(file_to_output, "w") as txt_file:
#    pass

# write results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
