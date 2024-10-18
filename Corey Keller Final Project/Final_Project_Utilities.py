"""
Author: Corey Keller
File Name: finalProjectUtilities.py
File Created: 4/10/2024
Purpose: Store various functions to be used among all of the user modules.
"""
#put csv information into array
def csvToArray(USERPATHNAME,USERCSVFILE,userEmptyArray):
    usersFileRead=open("./"+USERPATHNAME+"/"+USERCSVFILE, "r")
    next(usersFileRead)
    for row in usersFileRead:
        splitValues=row.strip().split(",")
        userEmptyArray.append(splitValues)
    usersFileRead.close()
    return userEmptyArray

#login verification
def loginPrompt(loginArray):
    import sys
    
    #create index variables
    USERNAMEINDEX=0
    PASSWORDINDEX=1
    MAXATTEMPTS=5
    
    #begin verification
    for loginAttempt in range(MAXATTEMPTS):
        enterUsername=input("Please enter your username.\n")
        print("---------------------------------------")
        enterPassword=input("Please enter your password.\n")
        print("---------------------------------------")
        #loop to check list of logins for matching username and password
        for item in loginArray:
            if item[USERNAMEINDEX]==enterUsername and item[PASSWORDINDEX]==enterPassword:
                print("Hello "+item[USERNAMEINDEX]+".\n")
                return item[USERNAMEINDEX]
        print("Incorrect username or password.\n"
              "---------------------------------------")
    print("Maxium amount of login attempts reached. Please try again later.\n"
          "---------------------------------------")
    #ends file execution after 5 incorrect inputs
    sys.exit()

#csv file creation
def csvFileCreateStudent(path,fileName):
    fileWrite=open("./"+path+"/"+fileName,"w")
    fileHeader=["Username","Password","FirstName","LastName\n"]
    fileWrite.write(",".join(fileHeader))
    fileWrite.close
def csvFileCreateInstructor(path,fileName):
    fileWrite=open("./"+path+"/"+fileName,"w")
    fileHeader=["Username","Password","FirstName","LastName","Title\n"]
    fileWrite.write(",".join(fileHeader))
    fileWrite.close
def csvFileCreateCourses(path,fileName):
    fileWrite=open("./"+path+"/"+fileName,"w")
    fileHeader=["Course Number","Course Title","Instructor\n"]
    fileWrite.write(",".join(fileHeader))
    fileWrite.close
def csvFileCreateEnrollment(path,fileName):
    fileWrite=open("./"+path+"/"+fileName,"w")
    fileHeader=["Username","Course Number\n"]
    fileWrite.write(",".join(fileHeader))
    fileWrite.close

#check for entity exist
def entityExistCheck(entity,loginArray,ENTITYINDEX):
    entityExists=False
    for item in loginArray:
        if item[ENTITYINDEX]==entity:
            entityExists=True
            break
    return entityExists

#create student object from username
def studentArrayInfoToStudentObject(studentUsername,loginArray):
    from Classes.Student_Class import Student
    STUDENTUSERNAMEINDEX=0
    STUDENTPASSWORDINDEX=1
    STUDENTFIRSTNAMEINDEX=2
    STUDENTLASTNAMEINDEX=3
    for student in loginArray:
        if student[STUDENTUSERNAMEINDEX]==studentUsername:
            addedStudent=Student(student[STUDENTUSERNAMEINDEX],student[STUDENTPASSWORDINDEX],student[STUDENTFIRSTNAMEINDEX],student[STUDENTLASTNAMEINDEX])
            return addedStudent

#create instructor object from username
def instructorArrayInfoToInstructorObject(instructorUsername,loginArray):
    from Classes.Instructor_Class import Instructor
    INSTRUCTORUSERNAMEINDEX=0
    INSTRUCTORPASSWORDINDEX=1
    INSTRUCTORFIRSTNAMEINDEX=2
    INSTRUCTORLASTNAMEINDEX=3
    INSTRUCTORTITLEINDEX=4
    for instructor in loginArray:
        if instructor[INSTRUCTORUSERNAMEINDEX]==instructorUsername:
            addedInstructor=Instructor(instructor[INSTRUCTORUSERNAMEINDEX],instructor[INSTRUCTORPASSWORDINDEX],instructor[INSTRUCTORFIRSTNAMEINDEX],
                                       instructor[INSTRUCTORLASTNAMEINDEX],instructor[INSTRUCTORTITLEINDEX])
            return addedInstructor

#create course object from course number
def courseArrayInfoToCourseObject(courseNumber,courseLoginArray,instructorLoginArray):
    from Classes.Instructor_Class import Instructor
    from Classes.Course_Class import Course
    INSTRUCTORUSERNAMEINDEX=0
    COURSENUMBERINDEX=0
    COURSETITLEINDEX=1
    COURSEINSTRUCTORINDEX=2
    for course in courseLoginArray:
        if course[COURSENUMBERINDEX]==courseNumber:
            for instructor in instructorLoginArray:
                if instructor[INSTRUCTORUSERNAMEINDEX]==course[COURSEINSTRUCTORINDEX]:
                    courseInstructor=instructorArrayInfoToInstructorObject(instructor[INSTRUCTORUSERNAMEINDEX],instructorLoginArray)
                    addedCourse=Course(course[COURSENUMBERINDEX],course[COURSETITLEINDEX],courseInstructor)
    return addedCourse

#check for exisiting enrollment
def enrollmentCheck(enrollmentInfoArray,usernameInput,courseNumberInput):
    ENROLLMENTUSERNAMEINDEX=0
    ENROLLMENTCOURSENUMBERINDEX=1
    studentAlreadyEnrolled=False
    for enrollment in enrollmentInfoArray:
            if enrollment[ENROLLMENTUSERNAMEINDEX]==usernameInput and enrollment[ENROLLMENTCOURSENUMBERINDEX]==courseNumberInput:
                studentAlreadyEnrolled=True
    return studentAlreadyEnrolled

#add student
def addStudent(USERPATHNAME,USERCSVFILE):
    from Classes.Student_Class import Student

    #create variables
    studentLoginArray=[]
    USERNAMEINDEX=0

    #create array from student csv file
    csvToArray(USERPATHNAME,USERCSVFILE,studentLoginArray)

    #begin asking for student information
    while True:
        usernameInput=input("Please enter the student's username."
                            " The username must not match the username of any other student.\n")
        print("---------------------------------------")

        #begin checking for existing usernames
        usernameCheck=entityExistCheck(usernameInput,studentLoginArray,USERNAMEINDEX)
        if usernameCheck:
            print("Username already taken.\n"
                  "---------------------------------------")
        else:
            break
        
    passwordInput=input("Please enter the student's password.\n")
    print("---------------------------------------")

    firstNameInput=input("Please enter the student's first name.\n")
    print("---------------------------------------")

    lastNameInput=input("Please enter the student's last name.\n")
    print("---------------------------------------")

    #creation of student from inputs
    addedStudent=Student(usernameInput,passwordInput,firstNameInput,lastNameInput)
    
    #ask if info looks correct
    while True:
        print(addedStudent)
        print("---------------------------------------")
        askForCorrection=input("Does the student information look correct?\n"
                               "If not enter the corresponding number with the incorrect information from the list below or type 'Done' to add the student. Type 'Cancel' to not add the student and cancel the action.\n"
                               "1. Username\n"
                               "2. Password\n"
                               "3. First name\n"
                               "4. Last name\n")
        print("---------------------------------------")

        if askForCorrection=="1":
            newUsername=input("Please enter the username again.\n")
            print("---------------------------------------")
            if any(item[USERNAMEINDEX]==newUsername for item in studentLoginArray):
                print("Username already taken. Please enter a different username.\n"
                      "---------------------------------------")
            else:
                addedStudent.setUsername(newUsername)

        elif askForCorrection=="2":
            newPassword=input("Please enter the password.\n")
            print("---------------------------------------")
            addedStudent.setPassword(newPassword)

        elif askForCorrection=="3":
            newFirstName=input("Please enter the student's first name.\n")
            print("---------------------------------------")
            addedStudent.setFirstName(newFirstName)

        elif askForCorrection=="4":
            newLastName=input("Please enter the student's last name.\n")
            print("---------------------------------------")
            addedStudent.setLastName(newLastName)

        elif askForCorrection.lower()=="done":
            #write the student to the csv file
            fileWriteStudent=open("./"+USERPATHNAME+"/"+USERCSVFILE, "a")
            fileWriteStudent.write(addedStudent.username+",")
            fileWriteStudent.write(addedStudent.password+",")
            fileWriteStudent.write(addedStudent.firstName+",")
            fileWriteStudent.write(addedStudent.lastName+"\n")
            fileWriteStudent.close()
            return
        
        elif askForCorrection.lower()=="cancel":
            return
        
        else:
            print("Invalid option.\n"
                  "---------------------------------------")
            continue

#add instructor
def addInstructor(USERPATHNAME,USERCSVFILE):
    from Classes.Instructor_Class import Instructor

    #create variables
    instructorLoginArray=[]
    USERNAMEINDEX=0

    #create array from instructor csv file
    csvToArray(USERPATHNAME,USERCSVFILE,instructorLoginArray)

    #begin asking for instructor information
    while True:
        usernameInput=input("Please enter the instructor's username."
                            " The username must not match the username of any other instructor.\n")
        print("---------------------------------------")
        #begin checking for existing usernames
        usernameCheck=entityExistCheck(usernameInput,instructorLoginArray,USERNAMEINDEX)
        if usernameCheck:
            print("Username already taken."
                  "---------------------------------------")
        else:
            break

    passwordInput=input("Please enter the instructor's password.\n")
    print("---------------------------------------")

    while True:
        titleInput=input("Please enter the instructor's title from the list below.\n"
                    "---------------------------------------\n"
                     "1. Assistant Professor\n"
                     "2. Associate Professor\n"
                     "3. Professor\n")
        if titleInput=="Assistant Professor" or titleInput=="Associate Professor" or titleInput=="Professor":
            print("---------------------------------------")
            break
        else:
            print("Invalid input for title. Please try again.\n"
                  "---------------------------------------")
            
    firstNameInput=input("Please enter the instructor's first name.\n")
    print("---------------------------------------")

    lastNameInput=input("Please enter the instructor's last name.\n")
    print("---------------------------------------")

    #creation of student from inputs
    addedInstructor=Instructor(usernameInput,passwordInput,firstNameInput,lastNameInput,titleInput)
    
    #ask if info looks correct
    while True:
        print(addedInstructor)
        print("---------------------------------------")
        askForCorrection=input("Does the instructor information look correct?"
                               "If not enter the corresponding number with the incorrect information from the list below or type 'Done' to add the student. Type 'Cancel' to not add the instructor and cancel the action.\n"
                               "1. Username\n"
                               "2. Password\n"
                               "3. First name\n"
                               "4. Last name\n"
                               "5. Title\n")
        print("---------------------------------------")

        if askForCorrection=="1":
            newUsername=input("Please enter the username again.\n")
            print("---------------------------------------")
            if any(item[USERNAMEINDEX]==newUsername for item in instructorLoginArray):
                print("Username already taken. Please enter a different username."
                      "---------------------------------------")
            else:
                addedInstructor.setUsername(newUsername)

        elif askForCorrection=="2":
            newPassword=input("Please enter the password.\n")
            print("---------------------------------------")
            addedInstructor.setPassword(newPassword)

        elif askForCorrection=="3":
            newFirstName=input("Please enter the instructor's first name.\n")
            print("---------------------------------------")
            addedInstructor.setFirstName(newFirstName)

        elif askForCorrection=="4":
            newLastName=input("Please enter the instructor's last name.\n")
            print("---------------------------------------")
            addedInstructor.setLastName(newLastName)

        elif askForCorrection=="5":
            while True:
                newTitle=input("Please enter the instructor's title.\n")
                print("---------------------------------------")
                if newTitle=="Assistant Professor" or newTitle=="Associate Professor" or newTitle=="Professor":
                    break
                else:
                    print("Invalid title option. Please try again.\n"
                          "---------------------------------------")
                    
        elif askForCorrection.lower()=="done":
            #write the instructor to the csv file
            fileWriteInstructor=open("./"+USERPATHNAME+"/"+USERCSVFILE, "a")
            fileWriteInstructor.write(addedInstructor.username+",")
            fileWriteInstructor.write(addedInstructor.password+",")
            fileWriteInstructor.write(addedInstructor.firstName+",")
            fileWriteInstructor.write(addedInstructor.lastName+",")
            fileWriteInstructor.write(addedInstructor.title+"\n")
            fileWriteInstructor.close()
            return
        
        elif askForCorrection.lower()=="cancel":
            return
        
        else:
            print("Invalid option.\n"
                  "---------------------------------------")
            continue

#add course
def addCourse(COURSEPATHNAME,COURSECSVFILE,INSTRUCTORPATHNAME,INSTRUCTORCSVFILE):
    from Classes.Course_Class import Course

    #create variables
    courseInfoArray=[]
    instructorInfoArray=[]
    COURSENUMBERINDEX=0
    INSTRUCTORUSERNAMEINDEX=0

    #create array of courses and instructors to use for checking
    csvToArray(COURSEPATHNAME,COURSECSVFILE,courseInfoArray)
    csvToArray(INSTRUCTORPATHNAME,INSTRUCTORCSVFILE,instructorInfoArray)

    #begin asking for course information
    courseTitleInput=input("Please enter the course name.\n")
    print("---------------------------------------")

    while True:
        courseInstructorInput=input("Please enter the username of the instructor teaching the course.\n")
        print("---------------------------------------")
        #check if instructor exists
        instructorCheck=entityExistCheck(courseInstructorInput,instructorInfoArray,INSTRUCTORUSERNAMEINDEX)
        if instructorCheck:
            break
        else:
            print("Instructor not found. Please check for correct username.\n"
                    "---------------------------------------")
            
    #create instructor from the login array for input in the course class constructor
    addedInstructor=instructorArrayInfoToInstructorObject(courseInstructorInput,instructorInfoArray)

    while True:
        courseNumberInput=input("Please enter the unique course number.\n"
                                "This number can not match the number of any other course number.\n")
        print("---------------------------------------")
        courseNumberHaveNumber=courseNumberInput.isdigit()
        if courseNumberHaveNumber:
            pass
        else:
            print("Course number must contain only digits. Please try again with only digits.\n"
                  "---------------------------------------")
            continue
        #check if course number is unique
        courseNumberCheck=entityExistCheck(courseNumberInput,courseInfoArray,COURSENUMBERINDEX)
        if courseNumberCheck:
            print("This course number already exists. Please enter the course number again.\n"
                    "---------------------------------------")
        else:
            break
    
    #create course object with inputs
    addedCourse=Course(courseNumberInput,courseTitleInput,addedInstructor)
    
    #begin asking if information looks correct and allow for correction
    while True:
        print(addedCourse)
        print("---------------------------------------")
        askForCorrection=input("Does the following course and instructor information look correct?\n"
                               "If not, please choose the correspsonding number with the incorrect information from the list below, or type 'Done' to add the course. Type 'Cancel' to not add the course and cancel the action.\n"
                               "1. Course Title\n"
                               "2. Course Number\n"
                               "3. Instructor\n")
        print("---------------------------------------")

        if askForCorrection=="1":
            newCourseTitle=input("Please enter the course title.\n")
            print("---------------------------------------")
            addedCourse.setCourseTitle(newCourseTitle)

        elif askForCorrection=="2":
            while True:
                newCourseNumber=input("Please enter the unique course number. This number can not match any other course number.\n")
                print("---------------------------------------")
                newCourseNumberHaveDigits=newCourseNumber.isdigit()
                if newCourseNumberHaveDigits:
                    pass
                else:
                    print("Course number must contain only digits. Please try again with only digits in the course number.\n"
                          "---------------------------------------")
                newCourseNumberCheck=entityExistCheck(newCourseNumber,courseInfoArray,COURSENUMBERINDEX)
                if newCourseNumberCheck:
                    print("This course number already exists. Please enter the course number again.\n"
                    "---------------------------------------")
                else:
                    break
            addedCourse.setCourseNumber(newCourseNumber)

        elif askForCorrection=="3":
            while True:
                newCourseInstructor=input("Please enter the username of the instructor teaching this course.\n")
                print("---------------------------------------")
                newCourseInstructorCheck=entityExistCheck(newCourseInstructor,instructorInfoArray,INSTRUCTORUSERNAMEINDEX)
                if newCourseInstructorCheck:
                    break
                else:
                    print("Instructor not found. Please check for the correct username.\n"
                        "---------------------------------------")
            newInstructor=instructorArrayInfoToInstructorObject(newCourseInstructor,instructorInfoArray)
            addedCourse.setInstructor(newInstructor)

        elif askForCorrection.lower()=="done":
            #write the course to the csv file
            fileWriteCourse=open("./"+COURSEPATHNAME+"/"+COURSECSVFILE, "a")
            fileWriteCourse.write(addedCourse.courseNumber+",")
            fileWriteCourse.write(addedCourse.courseTitle+",")
            fileWriteCourse.write(addedCourse.instructor.username+"\n")
            fileWriteCourse.close()
            return
        
        elif askForCorrection.lower()=="cancel":
            return
        
        else:
            print("Invalid option.\n"
                  "---------------------------------------")
            continue

#add enrollment
def addEnrollment(ENROLLMENTPATHNAME,ENROLLMENTCSVFILE,STUDENTPATHNAME,STUDENTCSVFILE,COURSEPATHNAME,COURSECSVFILE):
    #create variables
    enrollmentInfoArray=[]
    studentInfoArray=[]
    courseInfoArray=[]
    STUDENTUSERNAMEINDEX=0
    COURSENUMBERINDEX=0

    #populate arrays
    csvToArray(ENROLLMENTPATHNAME,ENROLLMENTCSVFILE,enrollmentInfoArray)
    csvToArray(STUDENTPATHNAME,STUDENTCSVFILE,studentInfoArray)
    csvToArray(COURSEPATHNAME,COURSECSVFILE,courseInfoArray)

    #begin asking for enrollment information
    while True:

        while True:
            studentUsernameInput=input("Please enter the username of the student enrolling or type 'Done' to exit the enrollment process.\n")
            print("---------------------------------------")
            if studentUsernameInput.lower()=="done":
                return
            studentUsernameExist=entityExistCheck(studentUsernameInput,studentInfoArray,STUDENTUSERNAMEINDEX)
            if studentUsernameExist:
                break
            else:
                print("Student not found. Please check the username again.\n"
                    "---------------------------------------")
                
        while True:
            courseNumberInput=input("Please enter the course number of the course "+studentUsernameInput+" is enrolling in or type 'done' to exit the enrollment process.\n")
            print("---------------------------------------")
            if courseNumberInput.lower()=="done":
                return
            courseNumberExists=entityExistCheck(courseNumberInput,courseInfoArray,COURSENUMBERINDEX)
            if courseNumberExists:
                break
            else:
                print("Course number not found. Please check the unique number of the course.\n"
                    "---------------------------------------")
        
        #check for current student enrollment
        enrollmentExists=enrollmentCheck(enrollmentInfoArray,studentUsernameInput,courseNumberInput)
        if enrollmentExists:
            print("Student already enrolled in course. Please check enrollment entries and try again.\n"
                      "---------------------------------------")
            continue
        else:
            break
                
    #ask if information looks correct
    while True:
        #check for existing enrollment each iteration, exit function if user trys to input existing username and course number in correct info block
        newEnrollmentExists=enrollmentCheck(enrollmentInfoArray,studentUsernameInput,courseNumberInput)
        if newEnrollmentExists:
            print("Student already enrolled in course. Please check enrollment entries and try again.\n"
                      "---------------------------------------")
            return

        print("Student Username: "+studentUsernameInput+"\n"
            "Course Number: "+courseNumberInput+"\n"
            "---------------------------------------")
        askForCorrection=input("Does the enrollment information look correct? If not, please choose the incorrect information from the corresponding number from the list below, or type 'Done' to add the course enrollment. Type 'Cancel' to not add the enrollment and cancel the action.\n"
                            "1. Student Username\n"
                            "2. Course Number\n")
        print("---------------------------------------")

        if askForCorrection=="1":
            while True:
                newStudentUsername=input("Please enter the enrolling student's username.\n")
                print("---------------------------------------")
                newStudentUsernameExists=entityExistCheck(newStudentUsername,studentInfoArray,STUDENTUSERNAMEINDEX)
                if newStudentUsernameExists:
                    studentUsernameInput=newStudentUsername
                    break
                else:
                    print("Student not found. Please check the username again.\n"
                          "---------------------------------------")
                    
        elif askForCorrection=="2":
            while True:
                newCourseNumber=input("Please enter the course number of the course "+studentUsernameInput+" is enrolling in.\n")
                print("---------------------------------------")
                newCourseNumberExists=entityExistCheck(newCourseNumber,courseInfoArray,COURSENUMBERINDEX)
                if newCourseNumberExists:
                    courseNumberInput=newCourseNumber
                    break
                else:
                    print("Course number not found. Please check the unique number of the course.\n"
                  "---------------------------------------")
                    
        elif askForCorrection.lower()=="done":
            fileWriteEnrollment=open("./"+ENROLLMENTPATHNAME+"/"+ENROLLMENTCSVFILE,"a")
            fileWriteEnrollment.write(studentUsernameInput+",")
            fileWriteEnrollment.write(courseNumberInput+"\n")
            fileWriteEnrollment.close()
            return
        
        elif askForCorrection.lower()=="cancel":
            return
        
        else:
            print("Invalid option.\n"
                  "---------------------------------------")
            continue

def seeStudentInfo(STUDENTPATHNAME,STUDENTCSVFILE):
    from Classes.Student_Class import Student

    #create variables
    studentInfoArray=[]
    STUDENTUSERNAMEINDEX=0
    STUDENTPASSWORDINDEX=1
    STUDENTFIRSTNAMEINDEX=2
    STUDENTLASTNAMEINDEX=3

    #populate array
    csvToArray(STUDENTPATHNAME,STUDENTCSVFILE,studentInfoArray)

    #begin prompt for student selection
    while True:
        seeStudentChoice=input("Please enter the username of the student you would like to see. For a list of all the students, type 'All'. Type 'Done' to exit the See Student action.\n")
        print("---------------------------------------")
        studentExists=entityExistCheck(seeStudentChoice,studentInfoArray,STUDENTUSERNAMEINDEX)

        if seeStudentChoice.lower()=="all":
            for student in studentInfoArray:
                viewedStudent=Student(student[STUDENTUSERNAMEINDEX],student[STUDENTPASSWORDINDEX],student[STUDENTFIRSTNAMEINDEX],student[STUDENTLASTNAMEINDEX])
                print(viewedStudent)
                print("---------------------------------------")

        elif seeStudentChoice.lower()=="done":
            return
        
        elif studentExists:
                for student in studentInfoArray:
                    if student[STUDENTUSERNAMEINDEX]==seeStudentChoice:
                        viewedStudent=Student(student[STUDENTUSERNAMEINDEX],student[STUDENTPASSWORDINDEX],student[STUDENTFIRSTNAMEINDEX],student[STUDENTLASTNAMEINDEX])
                        print(viewedStudent)
                        print("---------------------------------------")
                        
        else:
            print("Student not found.\n"
                      "---------------------------------------")
            continue

def seeInstructorInfo(INSTRUCTORPATHNAME,INSTRUCTORCSVFILE):
    from Classes.Instructor_Class import Instructor

    #create variables
    instructorInfoArray=[]
    INSTRUCTORUSERNAMEINDEX=0
    INSTRUCTORPASSWORDINDEX=1
    INSTRUCTORFIRSTNAMEINDEX=2
    INSTRUCTORLASTNAMEINDEX=3
    INSTRUCTORTITLEINDEX=4

    #populate array
    csvToArray(INSTRUCTORPATHNAME,INSTRUCTORCSVFILE,instructorInfoArray)

    #begin prompt for instructor selection
    while True:
        seeInstructorChoice=input("Please enter the username of the instructor you would like to see. For a list of all the instructors, type 'All'. Type 'Done' to exit the See Instructor action.\n")
        print("---------------------------------------")
        instructorExists=entityExistCheck(seeInstructorChoice,instructorInfoArray,INSTRUCTORUSERNAMEINDEX)

        if seeInstructorChoice.lower()=="all":
            for instructor in instructorInfoArray:
                viewedInstructor=Instructor(instructor[INSTRUCTORUSERNAMEINDEX],instructor[INSTRUCTORPASSWORDINDEX],instructor[INSTRUCTORFIRSTNAMEINDEX],instructor[INSTRUCTORLASTNAMEINDEX],instructor[INSTRUCTORTITLEINDEX])
                print(viewedInstructor)
                print("---------------------------------------")

        elif seeInstructorChoice=="done":
            return
        
        elif instructorExists:
            for instructor in instructorInfoArray:
                if instructor[INSTRUCTORUSERNAMEINDEX]==seeInstructorChoice:
                    viewedInstructor=Instructor(instructor[INSTRUCTORUSERNAMEINDEX],instructor[INSTRUCTORPASSWORDINDEX],instructor[INSTRUCTORFIRSTNAMEINDEX],instructor[INSTRUCTORLASTNAMEINDEX],instructor[INSTRUCTORTITLEINDEX])
                    print(viewedInstructor)
                    print("---------------------------------------")

        else:
            print("Instructor not found.\n"
                      "---------------------------------------")
            continue

def seeCourseInfo(COURSEPATHNAME,COURSECSVFILE,INSTRUCTORPATHNAME,INSTRUCTORCSVFILE):
    from Classes.Course_Class import Course
    from Classes.Instructor_Class import Instructor

    #create variables
    courseInfoArray=[]
    instructorInfoArray=[]
    COURSENUMBERINDEX=0
    COURSETITLEINDEX=1
    COURSEINSTRUCTORINDEX=2
    INSTRUCTORUSERNAMEINDEX=0

    #populate array
    csvToArray(COURSEPATHNAME,COURSECSVFILE,courseInfoArray)
    csvToArray(INSTRUCTORPATHNAME,INSTRUCTORCSVFILE,instructorInfoArray)

    #begin prompt for course selection
    while True:
        seeCourseChoice=input("Please enter the course number of the course you would like to see. For a list of all the courses, type 'All'. Type 'Done' to exit the See Course action.\n")
        print("---------------------------------------")
        courseExists=entityExistCheck(seeCourseChoice,courseInfoArray,COURSENUMBERINDEX)

        if seeCourseChoice.lower()=="all":
            for course in courseInfoArray:
                courseInstructorUsername=course[COURSEINSTRUCTORINDEX]
                courseInstructor=instructorArrayInfoToInstructorObject(courseInstructorUsername,instructorInfoArray)
                viewedCourse=Course(course[COURSENUMBERINDEX],course[COURSETITLEINDEX],courseInstructor)
                print(viewedCourse)
                print("---------------------------------------")

        elif seeCourseChoice.lower()=="done":
            return
        
        elif courseExists:
            for course in courseInfoArray:
                if course[COURSENUMBERINDEX]==seeCourseChoice:
                    courseInstructorUsername=course[COURSEINSTRUCTORINDEX]
                    courseInstructor=instructorArrayInfoToInstructorObject(courseInstructorUsername,instructorInfoArray)
                    viewedCourse=Course(course[COURSENUMBERINDEX],course[COURSETITLEINDEX],courseInstructor)
                    print(viewedCourse)
                    print("---------------------------------------")

        else:
            print("Course not found.\n"
                      "---------------------------------------")
            continue

def seeEnrollmentInfo(ENROLLMENTPATHNAME,ENROLLMENTCSVFILE,COURSEPATHNAME,COURSECSVFILE,STUDENTPATHNAME,STUDENTCSVFILE,INSTRUCTORPATHNAME,INSTRUCTORCSVFILE):
    from Classes.Course_Class import Course

    #create variables
    enrollmentInfoArray=[]
    studentInfoArray=[]
    courseInfoArray=[]
    instructorInfoArray=[]
    STUDENTUSERNAMEINDEX=0
    COURSENUMBERINDEX=0
    COURSETITLEINDEX=1
    COURSEINSTRUCTORINDEX=2
    ENROLLMENTUSERNAMEINDEX=0
    ENROLLMENTCOURSENUMBERINDEX=1

    #populate arrays
    csvToArray(ENROLLMENTPATHNAME,ENROLLMENTCSVFILE,enrollmentInfoArray)
    csvToArray(COURSEPATHNAME,COURSECSVFILE,courseInfoArray)
    csvToArray(STUDENTPATHNAME,STUDENTCSVFILE,studentInfoArray)
    csvToArray(INSTRUCTORPATHNAME,INSTRUCTORCSVFILE,instructorInfoArray)

    #begin prompt for enrollment selection
    while True:
        seeEnrollmentChoice=input("Please choose the corresponding number from the list below to see the information listed. Type 'Done' to exit the See Enrollment action\n"
                                  "1. See all students enrolled in a course\n"
                                  "2. See all courses a student is enrolled in\n")
        print("---------------------------------------")
        
        if seeEnrollmentChoice=="1":
            while True:
                enrollmentCourseNumberInput=input("Please enter the course number. Type 'Return' to choose enrollment viewing options again.\n")
                print("---------------------------------------")
                courseExists=entityExistCheck(enrollmentCourseNumberInput,courseInfoArray,COURSENUMBERINDEX)
                if courseExists:
                    for course in courseInfoArray:
                        if course[COURSENUMBERINDEX]==enrollmentCourseNumberInput:
                            courseInstructor=instructorArrayInfoToInstructorObject(course[COURSEINSTRUCTORINDEX],instructorInfoArray)
                            viewedCourse=Course(course[COURSENUMBERINDEX],course[COURSETITLEINDEX],courseInstructor)
                            print(viewedCourse)
                            print("---------------------------------------")

                    for enrollment in enrollmentInfoArray:
                        if enrollment[ENROLLMENTCOURSENUMBERINDEX]==enrollmentCourseNumberInput:
                            viewedStudent=studentArrayInfoToStudentObject(enrollment[ENROLLMENTUSERNAMEINDEX],studentInfoArray)
                            print(viewedStudent)
                            print("---------------------------------------")
                    break

                elif enrollmentCourseNumberInput.lower()=="return":
                    break

                else:
                    print("Course not found. Please check the number and try again.\n"
                          "---------------------------------------")
        
        elif seeEnrollmentChoice=="2":
            while True:
                enrollmentStudentUsernameInput=input("Please enter the student's username. Type 'Return' to choose enrollment viewing options again.\n")
                print("---------------------------------------")
                studentExists=entityExistCheck(enrollmentStudentUsernameInput,studentInfoArray,STUDENTUSERNAMEINDEX)
                if studentExists:
                    for student in studentInfoArray:
                        if student[STUDENTUSERNAMEINDEX]==enrollmentStudentUsernameInput:
                            viewedStudent=studentArrayInfoToStudentObject(student[STUDENTUSERNAMEINDEX],studentInfoArray)
                            print(viewedStudent)
                            print("---------------------------------------")

                    for enrollment in enrollmentInfoArray:
                        if enrollment[ENROLLMENTUSERNAMEINDEX]==enrollmentStudentUsernameInput:
                            for course in courseInfoArray:
                                if course[COURSENUMBERINDEX]==enrollment[ENROLLMENTCOURSENUMBERINDEX]:
                                    courseInstructor=instructorArrayInfoToInstructorObject(course[COURSEINSTRUCTORINDEX],instructorInfoArray)
                                    viewedCourse=Course(course[COURSENUMBERINDEX],course[COURSETITLEINDEX],courseInstructor)
                                    print(viewedCourse)
                                    print("---------------------------------------")
                    break
                elif enrollmentStudentUsernameInput.lower()=="return":
                    break
                else:
                    print("Student not found. Please check the username and try again.\n"
                          "---------------------------------------")
                    
        elif seeEnrollmentChoice.lower()=="done":
            return
        
        else:
            print("Invalid option, try again.\n"
                  "---------------------------------------")

#student enrollment view            
def studentSeeEnrollments(username,ENROLLMENTPATHNAME,ENROLLMENTCSVFILE,COURSEPATHNAME,COURSECSVFILE,INSTRUCTORPATHNAME,INSTRUCTORCSVFILE):
    from Classes.Course_Class import Course

    #index variables
    ENROLLMENTUSERNAMEINDEX=0
    ENROLLMENTCOURSENUMBERINDEX=1
    
    #create variables
    courseInfoArray=[]
    instructorInfoArray=[]
    enrollmentInfoArray=[]
    csvToArray(ENROLLMENTPATHNAME,ENROLLMENTCSVFILE,enrollmentInfoArray)
    csvToArray(COURSEPATHNAME,COURSECSVFILE,courseInfoArray)
    csvToArray(INSTRUCTORPATHNAME,INSTRUCTORCSVFILE,instructorInfoArray)

    for enrollment in enrollmentInfoArray:
                        if enrollment[ENROLLMENTUSERNAMEINDEX]==username:
                                    viewedCourse=courseArrayInfoToCourseObject(enrollment[ENROLLMENTCOURSENUMBERINDEX],courseInfoArray,instructorInfoArray)
                                    print(viewedCourse.stringReturnForStudents())
                                    print("---------------------------------------")

#instructor course teaching view
def instructorTeachingCourses(username,COURSEPATHNAME,COURSECSVFILE,INSTRUCTORPATHNAME,INSTRUCTORCSVFILE):
    from Classes.Course_Class import Course

    #index variables
    COURSENUMBERINDEX=0
    COURSEINSTRUCTORINDEX=2

    #create variables
    courseInfoArray=[]
    instructorInfoArray=[]
    csvToArray(COURSEPATHNAME,COURSECSVFILE,courseInfoArray)
    csvToArray(INSTRUCTORPATHNAME,INSTRUCTORCSVFILE,instructorInfoArray)
    
    #find and print info
    for course in courseInfoArray:
        if course[COURSEINSTRUCTORINDEX]==username:
            viewedCourse=courseArrayInfoToCourseObject(course[COURSENUMBERINDEX],courseInfoArray,instructorInfoArray)
            print(viewedCourse.stringReturnForInstructorCourses())
            print("---------------------------------------")