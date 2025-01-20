import csv
import os

# Define the path to the CSV file
file_path = os.path.join('Resources', 'election_data.csv')

# Initialize variables
total_votes = 0
candidates = {}

# Read the CSV file
with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Skip the header

    for row in csvreader:
        total_votes += 1
        candidate = row[2]  # Candidate's name is in the third column

        if candidate not in candidates:
            candidates[candidate] = 0
        candidates[candidate] += 1

# Print the candidates dictionary to check its contents (for debugging)
print("Candidates and their votes:", candidates)

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

# Print the results
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for result in results:
    print(result)
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export results to a text file
output_path = os.path.join('analysis', 'election_analysis.txt')
with open(output_path, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for result in results:
        txtfile.write(result + "\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")