# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 16:26:57 2018

@author: NO20039365
"""
import os 
import re
import nltk
import pandas as pd

#will contain file names with .txt extension
files = []

class ResumeClass():
    #current directory where all text files are located
    os.chdir("C:/Users/NO20039365/Desktop")
    file = None
    unCleanedFile = None
    tokens = None
    
    def __init__(self, fileName):
        self.file = fileName
    
    #reads file into program    
    def readFileIntoProgram(self):
        fileLines = open(self.file, encoding="utf8")
        
        #unformatted text file
        self.unCleanedFile = fileLines.readlines()
       
        fileLines.close
      
        
    def cleanOutNewLinesAndTabs(self):
        #takes unformatted text file and joins it into a string 
        str = ' '.join(self.unCleanedFile)
        
        #string from unformatted text is taken and individual words are places into arrays called tokens
        self.tokens = nltk.word_tokenize(str)
        
        #goes through list and removes \n and \t
        for i, s in enumerate(self.tokens):
            self.tokens[i] = s.strip()
            self.tokens[i] = re.sub(r"\t", ' ',s)
       
    
    #iterates through tokens list and looks for email    
    def emailFinder(self):
       
        #counter will keep track of @ characters index
        counter = 0
        for i in self.tokens:
            #index += 1
            if("@" == i):
                break
            counter += 1
            
        if(counter == len(self.tokens)):
            #if counter equals len of tokens then an email was not found
            email = "No email was found."
        else:
            #if @ charater was found then method takes the Strings to the right and 
            #left of it and concatenate the strings together to get the email
            email = self.tokens[counter - 1]
            email = email + self.tokens[counter]
            email = email + self.tokens[counter + 1]
            
        return email
    
    def firstName(self):
        #
        os.chdir("C:/Users/NO20039365/Documents/Python/PythonText")
        df = pd.read_csv('NameList.csv')
        #Will store String elements  only
        wordList = []
  
        alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        
        #goes through list and takes all the Strings elements
        for i in self.tokens:
            r= i.upper()
            rr = r[:1]
            if( rr in alpha):
                wordList.append(i)
      
        
        print(" ")
        found = False
        i = 0
        indexDf = 0
        #once string elements are found loop will compare each name to nameList to look for a match
        
        while(found == False):
        
            try:
                f = wordList[i][:1]
                name = df[f.upper()][indexDf]
                name = str(name)
                name = name.upper()
                if(wordList[i].upper() == name):
                    found = True
                    n = wordList[i]
                    break
                elif(10013 == indexDf):
                    i += 1
                    indexDf = 0
                else:
                    indexDf += 1
        
            except ValueError:
                i += 1
            
        return n
    
    #Returns phone numner in form of a tuple 
    def obtainPhoneNumber(self):
        #takes array list and joins it into a list
        str = " ".join(self.unCleanedFile)
        print("Phone Number:")
        #findall is used to recognize a 3-3-4 digit pattern
        phones = re.findall(r'(\()?((?(1)\d{3}(?=\))|\d{3}(?!\))))\)?[ -.]?(\d{3})[ -.]?(\d{4})',str)
        
        if(len(phones) == 0 ):
            #print("No phone number found")
            return 0
       # for i in phones:
            #print(i)
        else:
            return phones
   

#Looks for and returns Resume GPA, returns -1 if GPA was not found, returns value if found
    def searchForGPA(self):
        #Assumes there is no GPA in text so noGPA is set to True
        noGPA = True
       
    #Iterates through Tokens and looks for string GPA
        for i,ele in enumerate(self.tokens):
            if("GPA" in ele.upper()):
            #if string GPA is found noGPA becomes False
                noGPA = False
                #counter is the index value of GPA within the tokens array
                counter = i
        
        #
        if(noGPA == False):
          #While loop iterates through strings that come after GPA to look for GPA value
            while(True):
                #counter is incremented by one in order to look at the strings next to GPA
                x = self.tokens[counter + 1]
        
                try:
                    #takes value string next to GPA and if it converts to a float it is assumed that is the gpa value
                    gpaValue = float(x)
                    break
                except ValueError:
                    #if string next to GPA cannot convert to float it will increment to look at the next index
                    counter += 1
        elif(noGPA):
            #Gpa value was not found 
            gpaValue = -1
        
        return gpaValue
    
    #Creates a list with containing only strings, gets rid of any phone numbers, 
    #dates, GPA, and special charaters.
    #This method is not used in this prgram but it may come in hand later
    """def listContainingOnlyStrings(self):
        wordList = []
  
        alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
        for i in self.tokens:
            r= i.upper()
            rr = r[:1]
            if( rr in alpha):
                wordList.append(i)
    
        return wordList"""

#prints all .txt extension files within directory
def printTxtFilesInDir():
        
        for f in os.listdir(os.curdir):
            if(".txt" in f):
                files.append(f)
                print(f)

#returns true if the file user inputed exists within directory,
#returns false if it does not 
def verifyUsersInputIsInDir(usersInput):
        if(usersInput in files):
            return True
        else:
            return False

#if .txt extension is not specified, .txt is added to users input 
def addTxtExtentionToUserInput(userInput):
    l = len(userInput)
    s = l - 4
    #takes the last four substring characters of users input
    subString = userInput[s:l]
    
    #checks to see if string contains .txt extension, if it does not, extesnsion is added 
    if(subString != ".txt"):
        userInput = userInput + ".txt"
    
    return userInput





