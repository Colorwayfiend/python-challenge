import os
import csv
budget_data = os.path.join('Resources', 'budget_data.csv')

# declare lists from csv file
all_months = 0
all_pl = 0
value = 0
pl_changes = 0
dates = []
profits = []
# insert instructions for reader

with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)

    # Read through each row of data after the header
    csv_header = next(csvreader)

    # row 1 instructions

    all_months += 1
    all_pl += int(csv_header[1])
    # revenue = int(row[1])
    all_pl = int(csv_header[1])
    for row in csvreader:

        # find the difference then add to changes
        dates.append(row[0])
        all_months += 1
        all_pl += int(row[1])
        pl_changes = int(row[1])-value
        profits.append(int(row[1]))
        value = int(row[1])

    # net profit/ losses
    all_pl = all_pl + int(row[1])

    # Greatest increse in profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    # Greatest decrease in profits
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

    # average change
    print(type(profits[0]))
    print(sum(profits))
    print(len(profits))
    ave = round(sum(profits)/len(profits), 2)


print("Financial Analysis")
print("------------------")
print(f"All Months: {str(all_months)}")
print(f"Total: ${str(all_pl)}")
print(f"Average Change: ${str(round(ave, 2))}")
print(f"Greatest Increase: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease: {worst_date} (${str(greatest_decrease)})")

output = open("output.txt", "w")

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(all_months)}")
line4 = str(f"Total: ${str(all_pl)}")
line5 = str(f"Average Change: ${str(round(ave,2))}")
line6 = str(
    f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
line7 = str(
    f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(
    line1, line2, line3, line4, line5, line6, line7))
