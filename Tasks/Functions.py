"""This is examples of functions used in Python"""

#Searches for largest element in list
def Largest_element(arg_list):
    large_element = 0
    for i in arg_list:
        if i > large_element:
            large_element = i

    return large_element

#Reverse list function using for loop
def ReverseList(arg_list):

    rlist = []
    for i in arg_list:
        rlist.insert(0, i)

    return rlist

#Reverse list function using while loop
def ReverseListWhile(arg_list):

    rlist = []
    llist = len(arg_list)
    i = 0
    while i < llist:
        rlist.append(arg_list.pop())
        i = i+1

    return rlist

#Find x in list
def FindElement(arg_list):
    x = input("What do you want to check the list for?: ")
    if x in arg_list:
        print("Wowee, it is the list.")
    else:
        print("Negatory")

    return FindElement

#odd positions
#def OddPos(arg_list):
#    pos1 = 0
#    print(list[0])
#    print(p)
#    while p <= len(list):
#        p = list[pos1 + 1]

#    return OddPos

#for sum
def ForSum(arg_list):




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

if(numberFlag):
    valueToPrint = Largest_element(list)
    print("Largest value: ", valueToPrint)

listToPrint = ReverseListWhile(list)
print("Reversed list: ", listToPrint)

ElementFind = FindElement(list)

#PosOdd = OddPos(list)