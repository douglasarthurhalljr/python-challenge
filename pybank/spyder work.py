#import libraries
import os
import csv

#join our csv paths
budget_data = os.path.join(r"C:\Users\dougl\OneDrive\Desktop\Homework_03-Python_Instructions_PyBank_Resources_budget_data (2).csv")

# open and read csv
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    #set variables
    
    months = []
    profits = []
    revenue_change = []
    
    for rows in csv.reader:
        profits.append(int(rows[1]))
        months.append(len(rows[0]))
            
    
    for x in range(1, len(profits)):
        revenue_change.append((int(profits[x]) - int(profits[x-1])))
        
    revenue_average = sum(revenue_change) / len(revenue_change)
    
    # calculate total length of months
    total_months = len(months)

    # greatest increase in revenue
    greatest_increase = max(revenue_change)
    # greatest decrease in revenue
    greatest_decrease = min(revenue_change)

  
  
  
    print(f"total months {total_months}")
    print(f"WIN PERCENT: {win_percent}")
    print(f"LOSS PERCENT: {loss_percent}")
    print(f"DRAW PERCENT: {draw_percent}")
    print(f"{name} is a {type_of_wrestler}")