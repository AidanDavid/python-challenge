# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File.
Aidan David"""

import csv
import os

# files to load and output
file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("analysis", "election_analysis.txt")

# initialize variables
total_votes = 0
votes_dict = {}

# open csv file
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # skip first line
    header = next(reader)

    # loop through every row
    for row in reader:

        # get total votes
        total_votes = total_votes + 1

        votes_dict[row[2]] = votes_dict.get(row[2], 0) + 1

    winner = max(votes_dict, key=votes_dict.get)

    # form output
    output = "Election Results\n-------------------------\nTotal Votes: " + str(total_votes) + "\n-------------------------"

    for name, votes in votes_dict.items():
        output = output + "\n" + name + ": " + str(round(votes/total_votes*100, 3)) + "% (" + str(votes) + ")"

    output = output + "\n-------------------------" + "\n Winner: " + winner + "\n-------------------------"

    # print output in terminal
    print(output)

# write results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)