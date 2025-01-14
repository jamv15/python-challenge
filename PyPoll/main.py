# -*- coding: UTF-8 -*-
"""PyPoll Analysis."""

# Import necessary modules
import csv
import os

# Files to load and output
file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("analysis", "election_analysis.txt")

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
candidate_votes = {}  # Dictionary to track candidate names and vote counts

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0

        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    # Print the total vote count (to terminal)
    print(f"Total Votes: {total_votes}")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("\n")

    # Loop through the candidates to determine vote percentages and identify the winner
    winning_candidate = ""
    winning_count = 0

    for candidate, votes in candidate_votes.items():
        # Calculate the percentage of votes
        vote_percentage = (votes / total_votes) * 100

        # Print and save each candidate's vote count and percentage
        print(f"{candidate}: {vote_percentage:.3f}% ({votes})")
        txt_file.write(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")

        # Update the winning candidate if this one has more votes
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate

    # Generate and print the winning candidate summary
    print(f"\nWinner: {winning_candidate}")
    txt_file.write(f"\nWinner: {winning_candidate}\n")