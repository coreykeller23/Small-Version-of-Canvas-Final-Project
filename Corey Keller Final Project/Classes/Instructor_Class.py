"""
Author: Corey Keller
File Name: Instructor_Class.py
File Created: 4/17/2024
Purpose: Create the 'Instructor' class for the final project.
"""
from Classes.User_Class import User

class Instructor(User):
    #inherit all properties
    title="Assistant Professor" or "Associate Professor" or "Professor"

    #constructor
    def __init__(self,username,password,firstName,lastName,title):
        super().__init__(username,password,firstName,lastName)
        self.title=title

    #string return
    def __str__(self):
        return "Name: "+self.firstName+" "+self.lastName+"\n"+"Title: "+self.title+"\n"+"Username: "+self.username+"\n"+"Password: "+self.password
    
    #inherit all 'User' setters, create setter for 'title'
    def setTitle(self,title):
        self.title=title
    
    #inherit all 'User' getters, create getter for 'title'
    def getTitle(self):
        return self.title