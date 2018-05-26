# PyBank - Lucas Liang

import os
import csv
from datetime import datetime
from statistics import mean


source_csv =  "C:\\Users\\LENOVO USER\\Desktop\\USC Data Bootcamp\\3-HW, Python, 5-26-18\\budget_data_1.csv"

month = []
dictList= []
SortedList = []
dailyRevenue = {}

dailydiff = 0
totalrevenue = 0
total = 0

with open(source_csv,newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')

    next(csvreader, None)  # skip the headers

    for row in csvreader:
        
        #this is for file#1 due to date format mm-yy
        dictList.append([datetime.strptime(row[0],'%b-%y' ).strftime('%m-%d-%Y'),row[1], row[0]])
        
        #this is for file#2 due to date format mm-yyyy
        #dictList.append([datetime.strptime(row[0],'%b-%Y' ).strftime('%m-%d-%Y'),row[1], row[0]])
        
        #get the months for counting unique month later
        mmyy = row[0].split("-")
        month.append(str(mmyy[0]) + "-" + str(mmyy[1]))
        #sum daily revenue
        total += int(row[1])

SortedList =sorted(dictList, reverse=False)

for i in range(0,len(SortedList)):

    if i+1 < len(SortedList):

        dailydiff =int(SortedList[i+1][1]) -int(SortedList[i][1])

        dailyRevenue[SortedList[i+1][2]] = dailydiff

        totalrevenue = dailydiff + totalrevenue

dailymax =list(filter(lambda t: t[1]==max(dailyRevenue.values()), dailyRevenue.items()))[0][0]

dailymin =list(filter(lambda t: t[1]==min(dailyRevenue.values()), dailyRevenue.items()))[0][0]

print("Financial Analysis")
print("------------------")
print("Total Months: " + str(len(set(month))))
print('Total Revenue: ' + "$" + str(total))
print("Average Revenue Change: " + "$" + str(mean(dailyRevenue.values())))
print('Greatest Increase in Revenue: ' + "$" + str(max(dailyRevenue.values())) + ', Date: ' + dailymax)
print('Greatest Decrease in Revenue: ' + "$" + str(min(dailyRevenue.values())) + ', Date: ' + dailymin)

txt_header = str("Financial Analysis")
txt_line = str("------------------")
txt_total_months = str("Total Months: " + str(len(set(month))))
txt_total_revenue = str('Total Revenue: ' + "$" + str(total))
txt_avg_change = str("Average Revenue Change: " + "$" + str(mean(dailyRevenue.values())))
txt_max_change = str('Greatest Increase in Revenue: ' + "$" + str(max(dailyRevenue.values())) + ', Date: ' + dailymax)
txt_min_change = str('Greatest Decrease in Revenue: ' + "$" + str(min(dailyRevenue.values())) + ', Date: ' + dailymin)

#print(SortedList)
#print(str(total))
#print(month)
#print(mmyy)
#create txt file


output_file = os.path.join("financial_results_1.txt")  
text_result = open("financial_results_1.txt","w")

#/n goes to next line of text file
text_result.write(txt_header + " \n ")
text_result.write(txt_line + " \n ")
text_result.write(txt_total_months + " \n ")
text_result.write(txt_total_revenue + " \n ")
text_result.write(txt_avg_change + " \n ")
text_result.write(txt_max_change + " \n ")
text_result.write(txt_min_change + " \n ")
