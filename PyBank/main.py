# -*- coding: UTF-8 -*-
"""PyBank Analysis."""

# Dependencies
import csv
import os

# Files to load and output
file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("analysis", "budget_analysis.txt")

# Initialize variables
total_months = 0
total_net = 0
net_change_list = []
previous_profit = 0
greatest_increase = ["", 0]
greatest_decrease = ["", float("inf")]

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
    header = next(reader)

    for row in reader:
        total_months += 1
        total_net += int(row[1])

        # Calculate net change
        if total_months > 1:
            net_change = int(row[1]) - previous_profit
            net_change_list.append(net_change)

            # Check for greatest increase
            if net_change > greatest_increase[1]:
                greatest_increase[0] = row[0]
                greatest_increase[1] = net_change

            # Check for greatest decrease
            if net_change < greatest_decrease[1]:
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = net_change

        previous_profit = int(row[1])

# Calculate average net change
average_change = sum(net_change_list) / len(net_change_list)

# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)