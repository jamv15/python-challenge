import csv
import os

# Path to the CSV file
csv_path = os.path.join('Resources', 'budget_data.csv')

# Initialize variables
total_months = 0
net_total = 0
changes = []
previous_profit = None
greatest_increase = ("", 0)
greatest_decrease = ("", 0)

# Read the CSV file
with open(csv_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  
    
    # Skip the header

    for row in csvreader:
        total_months += 1
        profit = int(row[1])
        net_total += profit

        if previous_profit is not None:
            change = profit - previous_profit
            changes.append(change)

            if change > greatest_increase[1]:
                greatest_increase = (row[0], change)
            if change < greatest_decrease[1]:
                greatest_decrease = (row[0], change)

        previous_profit = profit

# Calculate average change
average_change = sum(changes) / len(changes)

# Print results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Export results to a text file
with open(os.path.join('analysis', 'financial_analysis.txt'), 'w') as f:
    f.write("Financial Analysis\n")
    f.write("----------------------------\n")
    f.write(f"Total Months: {total_months}\n")
    f.write(f"Total: ${net_total}\n")
    f.write(f"Average Change: ${average_change:.2f}\n")
    f.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    f.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")