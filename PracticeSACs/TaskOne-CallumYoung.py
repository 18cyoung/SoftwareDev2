#X value is used to end the loops once the desired value is achieved
x = 0

while x == 0:
    #ask for the value to assign to r
    r = input("What is your Gender? (Enter 'M' or 'F'): ")
    if r == "M":
        r = 0.68
        #increase x value to end loop
        x = 1
    elif r == "F":
        r = 0.55
        x = 1
    else:
        print("Please enter 'M' or 'F'")

while x == 1:
    #ask for the value to assign to W
    W = input("What is your weight? (Enter in Kg): ")
    try:
        #test if W is a float
        W = float(W)
        #test if W is positive
        if W >= 0:
            x=2
        #if W isn't positive print and retry
        else:
            print("Enter a positive integer.")
    except:
        # if there is an exception in required data retry loop
        print("Enter a positive integer.")

while x == 2:
    #ask for the value to assign to t
    t = input("How long since you started drinking? (Enter in hours): ")
    try:
        t = float(t)
        if t >= 0:
            x = 3
        else:
            print("Enter a positive integer.")
    except:
        print("Enter a positive integer.")

while x == 3:
    #ask for the value to assign to A
    A = input("How many standard drinks did you consume? (In total): ")
    try:
        A = float(A)
        if A >= 0:
            x = 4
        else:
            print("Enter a positive integer.")
    except:
        print("Enter a positive integer.")

while x == 4:
    #ask for the value to assign to D
    D = input("What is your driving status? (Enter 'L', 'P' or 'FL': ")
    if D == "L":
        x = 5
    elif D == "P":
        x = 5
    elif D == "FL":
        x = 5
    else:
        print("Please enter 'L', 'P' or 'FL'.")

A = 10*A
W = W*1000

#Calculate the BAC using equation
BAC = round((A/(r*W))*100-(0.00015*t),2)

#Inform user of BAC
print("Your Blood Alcohol Concentration is:" , BAC)

#Test if penalties needed for all the listed scenarios
if D == "L" or D == "P" and BAC > 0:
    print("Licence cancelled and interlock device installed for a minimum of 6 months.")

if D == "FL" and 0.05<BAC<0.07:
    print("Will be fined and incur 10 demerit points.")

if D == "FL" and BAC >= 0.07:
    print("Licence cancelled and interlock device installed for a minimum of 6 months.")
