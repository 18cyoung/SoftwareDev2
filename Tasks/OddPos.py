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


def OddPos(list):
    x = 0
    print(list[x])

    while x <= len(list):
        if x <= len(list):
            x = x+2
            if x < len(list):
                print(list[x])

    return OddPos

print(OddPos(list))