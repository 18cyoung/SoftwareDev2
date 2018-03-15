"""
Author: Callum Young
Date: 15/03/2018
version: 1.0
This code will provide the user with a menu listing all the functions they can choose to use.
The functions will allow the user to print the dictionary, search for terms within the dictionary, add new terms,
delete terms and save the dictionary to an external file. All the functions should be accessible through the file
"""

EnglishList = []
FrenchList = []
Dictionary = []


#This function will open the file the user searches for (if found) and assign the correct terms to the correct lists
#The variable name is FileName, which is used to search for and open the correct file
def FileRead():
    z = 0
    while z == 0:
        try:
            #user enters the file they are looking for
            FileName = input("Enter the file name: ")
            #file is opened to be read
            LangDict = open(FileName, 'r')
            z = 1
        except:
            #if filename is not found, exit
            print("file does not exist.")
            exit(1)

    #breaks down file into the needed lists
    for line in LangDict:
        line = line.strip('\n')
        line = line.split(',')
        EnglishList.append(line[0])
        FrenchList.append(line[1])
        Dictionary.append(line[0:2])
    return(FileRead)

#This function searches through the dictionary for a term the user is looking for, either in elgish or french
#The variable name is
def Search():
    print("Search Function")
    x = 0
    while x == 0:
        print("Leave blank to exit")
        Lang = input("Enter whether you would like to search for an (English) or (French) word: ")
        if Lang == "English":
            pos = 0
            word = input("What word are you looking for?: ")
            for i in EnglishList:
                if word == i:
                    print(Dictionary[pos])
        elif Lang == "French":
            word = input("What word are you looking for?: ")
            for i in FrenchList:
                pos = int(pos+1)
                if word == i:
                    print(Dictionary[pos])
        elif Lang == "":
            x = 1
        else:
            print("please enter (English) or (French)")
    return

#This function will allow the user to add a new english term with its corresponding french term to the dictionary
#The variable names are "English" and "French" which allows the terms to be assigned to the correct positions.
def AddNew():
    print("Add Translation")
    #Getting information from user
    print("Enter the translation details")
    English = input("English word: ")
    French = input("French translation: ")
    #Appending all data to lists
    EnglishList.append(English)
    FrenchList.append(French)
    #Appending lists to main dictionary
    Dictionary.append([English,French])
    print(Dictionary)
    return Dictionary

#This function allows the user to search for and delete a term and its translation from the dictionary
#The variable name is
def Delete():
    print("Delete translation")
    #uses search function to get position of term
    index = Search(Dictionary)
    #confirms users actions
    print("Are you sure you wish to delete this record? (Yes/No) ", Dictionary[index])
    userResponse = input(": ")
    #if user is sure, delete term and translation from list
    if(userResponse == "Yes"):
        Dictionary.pop(index)
    return Dictionary

#This function allows the user to save their changes that they made to the dictionary buy writing it to another file.
#The variable name is "entry" which helps write the terms to the correct positions.
def Save():
    print("Save file")
    #opens file to write
    f = open("Dictionary.txt", 'w')
    for entry in Dictionary:
        #write english term to first position
        EnglishList = entry[0]
        f.write(EnglishList[0])
        f.write(',')
        #writes french term to second position
        FrenchList = entry[1]
        f.write(FrenchList[0])
        f.write('\n')
    f.close()
    print("File saved")
    return 1



### MAIN BODY LOOP###
#defining x for the while loop

#run function to open correct file for reading
FileRead()

x = 0
while x == 0:
    #the value options for the menu, clearly listed for user to chosoe from
    menu = input('''
1. Print Dictionary
2. Search for a term
3. Add new term
4. Delete a term
5. Save dictionary
6. Terminate program    

    Selection:''')
    #testing if an integer is entered
    try:
        menu = int(menu)
        #choosing the function depending upon the value entered (E.g. 1-5)
        if menu == 1:
            print("The English words and their translations are:", Dictionary)
        elif menu == 2:
            Search()
        elif menu == 3:
            AddNew()
        elif menu == 4:
            Delete()
        elif menu == 5:
            Save()
        elif menu == 6:
            exit(1)
        #sending error message with how to correctly use the code
        else:
            print("Option not available, please enter the integers 1-6")
    except ValueError:
        print("Option not available, please enter the integers 1-6")
        print("---------------")