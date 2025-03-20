# Chapter 4 exercise
# Program: payroll2.py
# 3/3/25

# Payroll application that reads employee data from a file and outputs the payroll summary in tabular format

import time 
import os.path

# Input phase
fileName = input("Please type the name of the payroll file that you wish to process >> ")

#  While loop which is used to validate the input, making sure that the file name the user types actually exists
while os.path.isfile(fileName) == False:
  fileName = input("Sorry please enter a VALID payroll file name >> ")


# Out of the loop, which means the fileName is valid
print("Processing payroll file data...")
time.sleep(3)

# Processing and output phases
data = open(fileName, "r")

print()
print("%-18s%9s%9s%11s" % ("Last Name", "Wage", "Hours", "Earnings"))
print("-" * 50)

# FOR loop to go through the file line by line. Split up the data in each line. Place each component into tabular format and calculate the earning.
for line in data:
  # Break the line into indiviual string values
  dataArray = line.split()
  # Extract the last name from that array and store it
  name = dataArray[0]
  # Extract the wage from the array, convert it to a float and store
  wage = float(dataArray[1])
  # Extract the hours from the array, convert it to a float and store it
  hours = float(dataArray[2])
  # Next, calculate the earnings and store it
  earnings = wage * hours
  # Output the info into the tabular format
  print("%-18s%9.2f%9.2f%11.2f" % (name, wage, hours, earnings))

# Final sign-off message
data.close() 
input("\n\nEnd of file. Press ENTER to quit")
