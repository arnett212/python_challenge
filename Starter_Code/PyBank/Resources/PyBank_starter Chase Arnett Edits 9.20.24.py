# -*- coding: utf-8 -*-

"""PyBank Homework Starter File."""
import csv
import os

file_to_load = os.path.join('Starter_Code', 'PyBank', 'Resources' , 'budget_data.csv')

file_to_output = os.path.join("analysis", "budget_analysis.txt")

output_dir = os.path.dirname(file_to_output)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

if not os.path.exists(file_to_load):
    print("File not found:", file_to_load)
else:
    
    total_months = 0
    total_net = 0
    net_change_list = []
    month_of_change = []
    greatest_increase = ["", 0]
    greatest_decrease = ["", 9999999999999999999]

    with open(file_to_load) as financial_data:
        reader = csv.reader(financial_data)

        header = next(reader)

        first_row = next(reader)
        total_months += 1
        total_net += int(first_row[1])
        prev_net = int(first_row[1])

        for row in reader:
            total_months += 1
            total_net += int(row[1])
            net_change = int(row[1]) - prev_net
            prev_net = int(row[1])
            net_change_list.append(net_change)
            month_of_change.append(row[0])

            if net_change > greatest_increase[1]:
                greatest_increase[0] = row[0]
                greatest_increase[1] = net_change
            
            if net_change < greatest_decrease[1]:
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = net_change

    average_change = sum(net_change_list) / len(net_change_list)

    output = (
        f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${total_net}\n"
        f"Average Change: ${average_change:.2f}\n"
        f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
        f"Greatest Decrease in Losses: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
    )
    print(output)

    with open(file_to_output, "w") as txt_file:
        txt_file.write(output)
