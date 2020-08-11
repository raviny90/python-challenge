# Data_Import
import os
import csv

# Variables and values
total_months = 0
net_amount = 0
month_count = []
monthly_change = []

greatest_increase = 0
greatest_decrease = 0
greatest_increase_month = 0
greatest_decrease_month = 0

# Path For File
csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

# CSV File
with open(csvpath, 'r') as csvfile:
    
    # CSV Reader Specifies Delimiter, Variable That Holds Contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # The Header Row First - Read
    csv_header = next(csvreader)
    row = next(csvreader)
    
    # Calculate "Profit/Losses" & Set Variables For Rows - Total Number Of Months, Net Amount Of 
    previous_row = int(row[1])
    total_months += 1
    net_amount += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]
    
    # Each Row Of Data After The Header
    for row in csvreader:
        
        # Calculate Total Number Of Months Included In Dataset
        total_months += 1
        # Calculate Net Amount Of "Profit/Losses" Over The Entire Period
        net_amount += int(row[1])

        # Calculate Change From Current Month To Previous Month
        revenue_change = int(row[1]) - previous_row
        monthly_change.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])
        
        # Calculate The Greatest Increase
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
            
        # Calculate The Greatest Decrease
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]  
        
    # Calculate The Average & The Date
    average_change = sum(monthly_change)/ len(monthly_change)
    
    highest = max(monthly_change)
    lowest = min(monthly_change)

# Print Analysis
print(f"Financial Analysis")
print(f"----_-------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_amount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})")
print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})")
