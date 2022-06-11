# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 6. The winner of the election based on popular vote.

#Access our CSV data file
# Add our depencies
import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#open the election results and read the file
with open(file_to_load) as election_data:

    #read the file
    file_reader = csv.reader(election_data)




# Add data to election data

    #for row in file_reader:
    headers = next(file_reader)
    print(headers)



#close file 

