# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 08:51:16 2018

@author: NO20039365
"""

from Resume import *
from Resume import ResumeClass
import pandas as pd

userInput = None

 
while(True):
    
    printTxtFilesInDir()

    userInput = input("Which file would you like to work with? ")

    userInput = addTxtExtentionToUserInput(userInput)
    x = verifyUsersInputIsInDir(userInput)

    if(x):
        print("File was found.")
        break
    else:
        print("Invalid input try again.\n")
        

print("----------------------------------------------------------------")
    
#Creates object 
file = ResumeClass(userInput)
#Reads in the text file lines into program
file.readFileIntoProgram()

#cleans out new line and tabs from text document
file.cleanOutNewLinesAndTabs()

#returns email
email = file.emailFinder()
print("Email: \n" +email)

#returns name
name = file.firstName()
print("First Name:\n" +name+"\n")

#creates a tuple containing resume phone number
phone = file.obtainPhoneNumber()
if(phone == 0):
    print(phone)
else:
    print(phone)

#returns GPA
gpa = file.searchForGPA()
print("\nGPA:")
if(gpa == -1):
    print("No GPA was found.")
else:
    print(gpa)










