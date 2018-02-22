
x = 0
def FloatFunc(x):
    while x == 0:
        #ask for the value to assign to a
        a = input("Input text here:")
        try:
            a = float(a)
            if a >= 0:
                x = 1
            else:
                print("Requirement text here")
        except:
            print("Requirement text here")

FloatFunc(0)


###############


def StrFunc (x):
    while x == 0:
        #ask for the value to assign to a
        a = input("Input text here:")
        if a == "test1":
            a = 5 #Assign value depending on entry
            #increase x value to end loop
            x = 1
        elif a == "test2":
            a = 5 #Assign value depending on entry
            x = 1
        else:
            print("Requirement text here")

StrFunc(0)