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


def SumList(list):
    total = 0
    for i in list:
        total = total + i
    print(total)
    return SumList

SumList(list)
