import csv

# Set the path to the budget_data.csv file
file_path = "02-Homework\03-Python\Starter_Code\PyBank\Resources\budget_data.csv"

# Initialize variables
total_months = 0
net_total = 0
previous_profit_loss = 0
changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Read the budget_data.csv file
with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)  # Skip the header row

    # Loop through each row in the dataset
    for row in csvreader:
        # Increment total months
        total_months += 1

        # Calculate net total
        net_total += int(row[1])

        # Calculate change in profit/loss from the previous row
        change = int(row[1]) - previous_profit_loss

        # Store the current profit/loss for the next iteration
        previous_profit_loss = int(row[1])

        # Add the change to the list of changes
        if total_months > 1:
            changes.append(change)

        # Check for the greatest increase and decrease in profits
        if change > greatest_increase[1]:
            greatest_increase = [row[0], change]
        elif change < greatest_decrease[1]:
            greatest_decrease = [row[0], change]

# Calculate the average change
average_change = sum(changes) / len(changes)

# Format the analysis output
analysis_output = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_total}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})
Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})
"""

# Print the analysis to the terminal
print(analysis_output)

# Export the analysis to a text file
output_file = "financial_analysis.txt"
with open(output_file, "w") as textfile:
    textfile.write(analysis_output)

print(f"Analysis has been exported to {output_file}")
