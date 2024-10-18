"""
Author: Corey Keller
File Name: Instructor_Module.py
File Created: 4/24/24
Purpose: Perform the functions of an instructor in the Mini Canvas Program.
"""
import Final_Project_Utilities
import sys

#create variables
INSTRUCTORPATHNAME="Instructor Information"
INSTRUCTORCSVFILE="Instructor_Logins.csv"
COURSEPATHNAME="Course Information"
COURSECSVFILE="Course_List.csv"

#create instructor login array and populate array
instructorLoginArray=[]
Final_Project_Utilities.csvToArray(INSTRUCTORPATHNAME,INSTRUCTORCSVFILE,instructorLoginArray)

#prompt username and password entry to login as instructor
instructorUser=Final_Project_Utilities.loginPrompt(instructorLoginArray)

#begin prompt for instructor action
while True:
    instructorInputChoice=input("Choose the corresponding number of the action you wish to take from the list below. Type 'Exit' to exit the program.\n"
                             "1. See courses\n")
    
    if instructorInputChoice=="1":
        try:
            Final_Project_Utilities.instructorTeachingCourses(instructorUser,COURSEPATHNAME,COURSECSVFILE,INSTRUCTORPATHNAME,INSTRUCTORCSVFILE)
        except:
            print("Invalid option. Please try again\n"
              "---------------------------------------")
    elif instructorInputChoice.lower()=="exit":
        print("Thank you for visiting. We hope to see you again :)")
        sys.exit()
    else:
        print("Invalid option. Please try again\n"
              "---------------------------------------")