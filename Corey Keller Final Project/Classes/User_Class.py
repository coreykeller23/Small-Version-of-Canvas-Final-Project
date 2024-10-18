"""
Author: Corey Keller
File Name: User_Class.py
File Created: 4/17/2024
Purpose: Create the 'User' class for the final project.
"""

class User:
    username=""
    password=""
    firstName=""
    lastName=""

    #constructor
    def __init__(self,username,password,firstName,lastName):
        self.username=username
        self.password=password
        self.firstName=firstName
        self.lastName=lastName

    #string return
    def __str__(self):
        return ("Name: "+self.firstName+" "+self.lastName+"\n"+"Username: "+self.username+"\n"+"Password: "+self.password)
    
    #setters
    def setUsername(self,username):
        self.username=username
    def setPassword(self,password):
        self.password=password
    def setFirstName(self,firstName):
        self.firstName=firstName
    def setLastName(self,lastName):
        self.lastName=lastName
    
    #getters
    def getUsername(self):
        return self.username
    def getPassword(self):
        return self.password
    def getFirstName(self):
        return self.firstName
    def getLastName(self):
        return self.lastName