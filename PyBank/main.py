# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File.
Aidan David"""

import csv
import os

# files to load and output
file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("analysis", "budget_analysis.txt")

# initialize variables
total_months = 0
total_net = 0
months = 1
prev_val = 0
curr_val = 0
val_change = []
val_total = 0

# open csv file
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # skip header
    header = next(reader)

    # initialize max/min with first val
    line = next(reader)
    max_val, min_val = (line[0], int(line[1])), (line[0], int(line[1]))
    prev_val = int(line[1])

    # loop through every row
    for row in reader:

        # get number of months
        months = months + 1

        # calculate change in profit/loss
        curr_val = int(row[1])
        val_change = curr_val - prev_val

        # calculate total profit/loss
        val_total = val_total + curr_val

        # store the min/max value
        if curr_val > max_val[1]:
            max_val = (row[0], curr_val)
        if curr_val < min_val[1]:
            min_val = (row[0], curr_val)

        prev_val = curr_val

    # form output
    output = "Financial Analysis\n----------------------------\nTotal Months: " + str(months) + "\nTotal: $" + str(val_total) + "\nAverage Change: $" + str(round(val_change/months, 2)) + "\nGreatest Increase in Profits: " + max_val[0] + " ($"+ str(max_val[1]) + ")" + "\nGreatest Decrease in Profits: " + min_val[0] + " ($"+ str(min_val[1]) + ")"

    # print output in terminal
    print(output)

# write results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
