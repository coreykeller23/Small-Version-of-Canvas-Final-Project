"""
Author: Corey Keller
File Name: Student_Module.py
File Created: 4/22/24
Purpose: Perform the functions of a student in the Mini Cavas Program.
"""
import Final_Project_Utilities
import sys

#create variables
STUDENTPATHNAME="Student Information"
STUDENTCSVFILE="Student_Logins.csv"
INSTRUCTORPATHNAME="Instructor Information"
INSTRUCTORCSVFILE="Instructor_Logins.csv"
COURSEPATHNAME="Course Information"
COURSECSVFILE="Course_List.csv"
ENROLLMENTPATHNAME="Enrollment Information"
ENROLLMENTCSVFILE="Enrollment_List.csv"

#create student login array and populate array
studentLoginArray=[]
Final_Project_Utilities.csvToArray(STUDENTPATHNAME,STUDENTCSVFILE,studentLoginArray)

#prompt username and password entry to login as a student
studentUser=Final_Project_Utilities.loginPrompt(studentLoginArray)

#begin prompt for student actions
while True:
    studentInputChoice=input("Choose the corresponding number of the action you wish to take from the list below. Type 'Exit' to exit the program.\n"
                             "1. See enrollments\n")

    if studentInputChoice=="1":
        try:
            Final_Project_Utilities.studentSeeEnrollments(studentUser,ENROLLMENTPATHNAME,ENROLLMENTCSVFILE,COURSEPATHNAME,COURSECSVFILE,INSTRUCTORPATHNAME,INSTRUCTORCSVFILE)
        except:
            print("Unexpected error. Please try again.\n"
                  "---------------------------------------")
    elif studentInputChoice.lower()=="exit":
        print("Thank you for visiting. We hope to see you again :)")
        sys.exit()
    else:
        print("Invalid option. Please try again\n"
              "---------------------------------------")