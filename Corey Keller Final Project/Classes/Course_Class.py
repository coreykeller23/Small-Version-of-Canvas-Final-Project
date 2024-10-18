"""
Author: Corey Keller
File Name: Course_Class.py
File Created: 4/17/2024
Purpose: Create the 'Course' class for the final project.
"""
from Classes.Instructor_Class import Instructor

class Course:
    courseNumber=""
    courseTitle=""
    instructor=Instructor

    #constructor
    def __init__(self,courseNumber,courseTitle,instructor):
        self.courseNumber=courseNumber
        self.courseTitle=courseTitle
        self.instructor=instructor

    #str return
    def __str__(self):
        return "Course Title: "+self.courseTitle+"\n"+"Course Number: "+self.courseNumber+"\n"+"Instructor: "+str(self.instructor)
    
    #setters
    def setCourseNumber(self,courseNumber):
        self.courseNumber=courseNumber
    def setCourseTitle(self,courseTitle):
        self.courseTitle=courseTitle
    def setInstructor(self,instructor):
        self.instructor=instructor
    
    #getters
    def getCourseNumber(self):
        return self.courseNumber
    def getCourseTitle(self):
        return self.courseTitle
    def getInstructor(self):
        return self.instructor
    
    #additional methods
    def stringReturnForStudents(self):
        return "Course Title: "+self.courseTitle+"\n"+"Course Number: "+self.courseNumber+"\n"+"Instructor: "+self.instructor.firstName+" "+self.instructor.lastName
    
    def stringReturnForInstructorCourses(self):
        return "Course Title: "+self.courseTitle+"\n"+"Course Number: "+self.courseNumber