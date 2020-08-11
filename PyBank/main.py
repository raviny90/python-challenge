#Data_Import
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

#Path For File
csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

#csvFile - command to open
with open(csvpath, 'r') as csvfile:
    
    #Variables and csvReader Spec delimiter,
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #The Header Row First - Read
    csv_header = next(csvreader)
    row = next(csvreader)
    
    #"Profit&Losses" calculations & Setting Variables For Rows -total Number Of Months, Net Amount Of 
    previous_row = int(row[1])
    total_months += 1
    net_amount += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]
    
    #Each Row Of Data After The Header
    for row in csvreader:
        
        #Total Number Of Months Included In Dataset - calculation
        total_months += 1
        #Net Amount Of "Profit/Losses" Over The Entire Period - calculation
        net_amount += int(row[1])

        #Change From Current Month To Previous Month - calculation
        revenue_change = int(row[1]) - previous_row
        monthly_change.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])
        
        #The Greatest Increase - calculation
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
            
        #The Greatest Decrease - calculation
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]  
        
    #The Average & The Date - calculation
    average_change = sum(monthly_change)/ len(monthly_change)
    
    highest = max(monthly_change)
    lowest = min(monthly_change)

#Print breakdown Analysis
print(f"Financial Analysis")
print(f"----_-------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_amount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})")
print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})")

#File To Write To - specification
output_file = os.path.join('..', 'PyBank', 'Resources', 'budget_data_revised.text')

#Variables - Opening the File in "Write" Mode
with open(output_file, 'w',) as txtfile:

#New Data
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_amount}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})\n")
