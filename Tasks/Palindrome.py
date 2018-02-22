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

#palindrome
revlist = list[::-1]

print(list)
print(revlist)

if list == revlist:
    print("The list is a palindrome")
else:
    print("The list is not a palindrome")