"""
Author: Corey Keller
File Name: adminModule.py
File Created: 4/10/2024
Purpose: Perform the functions of an admin in the Mini Canvas program.
"""
import Final_Project_Utilities
import os
import sys

#create essential variables that wont change
STUDENTPATHNAME="Student Information"
STUDENTCSVFILE="Student_Logins.csv"
INSTRUCTORPATHNAME="Instructor Information"
INSTRUCTORCSVFILE="Instructor_Logins.csv"
COURSEPATHNAME="Course Information"
COURSECSVFILE="Course_List.csv"
ENROLLMENTPATHNAME="Enrollment Information"
ENROLLMENTCSVFILE="Enrollment_List.csv"
ADMINPATHNAME="Admin Information"
ADMINCSVFILE="Admin_Logins.csv"

#create array of usernames and passwords from Admin_Logins.csv
adminUsersArray=[]
Final_Project_Utilities.csvToArray(ADMINPATHNAME,ADMINCSVFILE,adminUsersArray)

#prompt username and password entry, checking for accuracy using the created array
adminUser=Final_Project_Utilities.loginPrompt(adminUsersArray)

#create the files for Student and Instructor logins, and Courses and Enrollement lists with appropriate paths, exception handling to make sure file runs on subsequent executions
studentPath=os.path.join(os.getcwd(), "./"+STUDENTPATHNAME)
teacherPath=os.path.join(os.getcwd(), "./"+INSTRUCTORPATHNAME)
coursePath=os.path.join(os.getcwd(),"./"+COURSEPATHNAME)
enrollmentPath=os.path.join(os.getcwd(),"./"+ENROLLMENTPATHNAME)
try:
    os.mkdir(teacherPath)
    os.mkdir(studentPath)
    os.mkdir(coursePath)
    os.mkdir(enrollmentPath)
    Final_Project_Utilities.csvFileCreateStudent(STUDENTPATHNAME,STUDENTCSVFILE)
    Final_Project_Utilities.csvFileCreateInstructor(INSTRUCTORPATHNAME,INSTRUCTORCSVFILE)
    Final_Project_Utilities.csvFileCreateCourses(COURSEPATHNAME,COURSECSVFILE)
    Final_Project_Utilities.csvFileCreateEnrollment(ENROLLMENTPATHNAME,ENROLLMENTCSVFILE)
except:
    pass

#begin prompt for admin actions
while True:
    adminActionChoice=input("What would you like to do today? Please choose the associated number to perform an action from the list below. Type 'Exit' to shut down the program.\n"
                            "---------------------------------------\n"
                            "1. Add student\n"
                            "2. Add instructor\n"
                            "3. Add course\n"
                            "4. Add an enrollment for a student\n"
                            "5. See student information\n"
                            "6. See instructor information\n"
                            "7. See course information\n"
                            "8. See enrollment information\n")
    print("---------------------------------------")

    if adminActionChoice=="1":
        try:
            Final_Project_Utilities.addStudent(STUDENTPATHNAME,STUDENTCSVFILE)
        except:
            print("Unexpected error. Please try again.\n"
                  "---------------------------------------")
            
    elif adminActionChoice=="2":
        try:
            Final_Project_Utilities.addInstructor(INSTRUCTORPATHNAME,INSTRUCTORCSVFILE)
        except:
            print("Unexpected error. Please try again.\n"
                  "---------------------------------------")
            
    elif adminActionChoice=="3":
        try:
            Final_Project_Utilities.addCourse(COURSEPATHNAME,COURSECSVFILE,INSTRUCTORPATHNAME,INSTRUCTORCSVFILE)
        except:
            print("Unexpected error. Please try again.\n"
                  "---------------------------------------")
            
    elif adminActionChoice=="4":
        try:
            Final_Project_Utilities.addEnrollment(ENROLLMENTPATHNAME,ENROLLMENTCSVFILE,STUDENTPATHNAME,STUDENTCSVFILE,COURSEPATHNAME,COURSECSVFILE)
        except:
            print("Unexpected error. Please try again.\n"
                  "---------------------------------------")
            
    elif adminActionChoice=="5":
        try:
            Final_Project_Utilities.seeStudentInfo(STUDENTPATHNAME,STUDENTCSVFILE)
        except:
            print("Unexpected error. Please try again.\n"
                  "---------------------------------------")
            
    elif adminActionChoice=="6":
        try:
            Final_Project_Utilities.seeInstructorInfo(INSTRUCTORPATHNAME,INSTRUCTORCSVFILE)
        except:
            print("Unexpected error. Please try again.\n"
                  "---------------------------------------")
            
    elif adminActionChoice=="7":
        try:
            Final_Project_Utilities.seeCourseInfo(COURSEPATHNAME,COURSECSVFILE,INSTRUCTORPATHNAME,INSTRUCTORCSVFILE)
        except:
            print("Unexpected error. Please try again.\n"
                  "---------------------------------------")
            
    elif adminActionChoice=="8":
        try:
            Final_Project_Utilities.seeEnrollmentInfo(ENROLLMENTPATHNAME,ENROLLMENTCSVFILE,COURSEPATHNAME,COURSECSVFILE,STUDENTPATHNAME,STUDENTCSVFILE,INSTRUCTORPATHNAME,INSTRUCTORCSVFILE)
        except:
            print("Unexpected error. Please try again.\n"
                  "---------------------------------------")
            
    elif adminActionChoice.lower()=="exit":
        print("Thank you for visiting. We hope to see you again :)")
        sys.exit()
        
    else:
        print("Invalid option. Please try again\n"
              "---------------------------------------")