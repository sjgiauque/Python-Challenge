	# Import os module	
	import os
	import csv
	
	# Map file location
	input_file = os.path.join(".", "Resources", "budget_data.csv")
	
	# Define "Loop" variables
	total_months = []
	total_profit = []
	monthly_profit_change = []
	 
	# Open, improved reading using CSV module
	with open(input_file,newline="") as budget:
	

	     # CSV reader specifies delimiter and variable that holds contents
	    csvreader = csv.reader(budget,delimiter=",") 
	

	    # Skip header
	    header = next(csvreader)  
	

	    # Loop through each row in the csv
	    for row in csvreader: 
	

	        # Append total months and total profit to their corresponding lists
	        total_months.append(row[0])
	        total_profit.append(int(row[1]))
	

	    # Loop through profits to calculate monthly change in profits
	    for i in range(len(total_profit)-1):
	        
	        # Calculate the difference between two months and append to monthly profit change
	        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
	        
	# Calculate max and min of the the montly profit change list
	max_increase_value = max(monthly_profit_change)
	max_decrease_value = min(monthly_profit_change)
	

	# Correlate max and min to the proper month using month list and index from max and min
	# Use the plus 1 at the end since month associated with change is the + 1 month or next month
	max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
	max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 
	

	# Print Statements
	print("Financial Analysis")
	print("----------------------------")
	print(f"Total Months: {len(total_months)}")
	print(f"Total: ${sum(total_profit)}")
	print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
	print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
	print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")
	

	# Define Print Statements output file location
	output_file = Path("Python-Challenge", "PyBank", "Financial_Analysis_Summary.txt")
	

	with open(output_file,"w") as file:
	    
	# Push/Write Printed Statements to Financial_Analysis_Summary 
	    file.write("Financial Analysis")
	    file.write("\n")
	    file.write("----------------------------")
	    file.write("\n")
	    file.write(f"Total Months: {len(total_months)}")
	    file.write("\n")
	    file.write(f"Total: ${sum(total_profit)}")
	    file.write("\n")
	    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
	    file.write("\n")
	    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
	    file.write("\n")
	    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")
	



