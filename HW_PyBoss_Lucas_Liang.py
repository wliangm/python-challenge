# HW PyBoss - Lucas Liang

import os
import csv


emp_id = []
first_name = []
last_name = []
emp_dob = []
last_ssn = []
state_abbrev = []

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


#this is for the fist population of data from employee_data1.csv
source_csv = os.path.join("..","C:/Users/LENOVO USER/Desktop/USC Data Bootcamp/3-HW, Python, 5-26-18","employee_data1.csv")


with open(source_csv,newline="") as csvfile:
        
    csvreader = csv.reader(csvfile,delimiter=",")
    
    next(csvreader)  # skip the headers
    
    for row in csvreader:
        #store employee_id
        emp_id.append(row[0])
        #split name into first and last and store them
        name = row[1].split(" ")
        first_name.append(str(name[0]))
        last_name.append(str(name[1]))
        #store employee_dob
        dob_date = row[2].split("-")
        emp_dob.append(str(dob_date[1]) + "/" + str(dob_date[1]) + "/" + str(dob_date[0]))
        #split ssn and store the last four digits
        ssn_split = row[3].split("-")
        last_ssn.append("***-**-" + str(ssn_split[2]))
        #get abbreviation and store them
        state = us_state_abbrev.get(str(row[4]))
        state_abbrev.append(str(state))

#this is for the second population of data from employee_data2.csv
source_csv_2 = os.path.join("..","C:/Users/LENOVO USER/Desktop/USC Data Bootcamp/3-HW, Python, 5-26-18","employee_data2.csv")

with open(source_csv_2,newline="") as csvfile2:
        
    csvreader2 = csv.reader(csvfile2,delimiter=",")
    
    next(csvreader2)  # skip the headers
    
    for row in csvreader2:
        #store employee_id
        emp_id.append(row[0])
        #split name into first and last and store them
        name = row[1].split(" ")
        first_name.append(str(name[0]))
        last_name.append(str(name[1]))
        #store employee_dob
        dob_date = row[2].split("-")
        emp_dob.append(str(dob_date[1]) + "/" + str(dob_date[1]) + "/" + str(dob_date[0]))
        #split ssn and store the last four digits
        ssn_split = row[3].split("-")
        last_ssn.append("***-**-" + str(ssn_split[2]))
        #get abbreviation and store them
        state = us_state_abbrev.get(str(row[4]))
        state_abbrev.append(str(state))
        
        
#zip all columns/arrays
revised_emp_list = zip(emp_id,first_name,last_name,emp_dob,last_ssn,state_abbrev)  


# save the combined output from data set 1 and 2
output_file = os.path.join("formatted_employee_data_1&2.csv")
# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w", newline="") as new_emp_file:
    writer = csv.writer(new_emp_file)
    #insert header
    writer.writerow(["Emp ID", "First Name", "Last Name","DOB","SSN","State"])
    #insert rows from revised_emp_list
    writer.writerows(revised_emp_list)


#testing purpose via print()
#print(emp_id)
#print(first_name)
#print(last_name)
#print(emp_dob)
#print(last_ssn)
#print(state_abbrev)

        