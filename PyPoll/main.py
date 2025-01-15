import csv
import os

# Path to the CSV file
csv_path = os.path.join('Resources', 'election_data.csv')

# Initialize variables
total_votes = 0
candidates = {}

# Read the CSV file
with open(csv_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  
    
    # Skip the header

    for row in csvreader:
        total_votes += 1
        candidate = row[2]

        if candidate not in candidates:
            candidates[candidate] = 0
        candidates[candidate] += 1

# Calculate percentages and determine the winner
winner = ""
winning_count = 0
results = []

for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    results.append(f"{candidate}: {percentage:.3f}% ({votes})")
    
    if votes > winning_count:
        winning_count = votes
        winner = candidate

# Print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {