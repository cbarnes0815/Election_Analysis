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

# Initialize a total vote counter 
total_votes = 0

# candidate options and candidate votes
candidate_options = [] #list
candidate_votes = {} #dictionary

# Winning candidate and Winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open the election results and read the file
with open(file_to_load) as election_data:

    #read the file
    file_reader = csv.reader(election_data)

    #Read the header row
    headers = next(file_reader)

    # Print each row of the CSV file 
    for row in file_reader:
        # Add the total votes count
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]
        

        # If candidate does not match and existing candidate...
        if candidate_name not in candidate_options:

        # 4. Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

        # Begin tracking the candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

    # Save the results to the Election data txt
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"--------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------------\n")
    print(election_results, end="")

    #Save the final vote count to the txt file

    txt_file.write(election_results)

        # Determine the percentage of the votes
        # 1. Iterate through the candidate list
    for candidate_name in candidate_votes:

        # Retrieve vote count of a candidate 
        votes = candidate_votes[candidate_name]

        # Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

    # Print each candidate's name, vote count, and percentage of votes
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        #Determine winning vote count and candidate
        
        #Determine if the votes is greater than the winning count
        if (votes> winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage

            # Set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name
    #Print the winning candidate, vote count and percentage 
    winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------\n")
    #print(winning_candidate_summary)



#close file 

