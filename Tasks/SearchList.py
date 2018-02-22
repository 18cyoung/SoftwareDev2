#MAIN BODY CODE
list = []
UI = "\n"
numberFlag = True
while (UI != ""):
    UI = input("Enter a value for the list: ")
    if (UI != ""):
        try:
            UI = float(UI)
        except ValueError:
            numberFlag = False
        list.append(UI)
        print("The current values are: ")
        print(list)

x = float(input("What do you want to search the list for? "))
if x in list:
    print(x,"is present")
else:
    print(x,"is not present")