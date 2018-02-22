x = 0

while x == 0:
    #ask for user to choose a unit type
    u = input("Please choose Imperial units (enter '1') or Metric units (enter '2'): ")
    if u == "1":
        u = 1 #Assign u value depending on entry
        #increase x value to end loop
        x = 1
    elif u == "2":
        u = 2 #Assign u value depending on entry
        x = 1
    else:
        #ask user to enter correct data if they did not
        print("Please enter either '1' or '2'.")

#if user chooses metric run this loop
if u == 2:
    while x == 1:
        #ask for the value to assign to weight
        w = input("What is your weight? (Kg): ")
        try:
            #test if float integer was entered
            w = float(w)
            #test if entered integer is positive integer
            if w >= 0:
                #raise x value to end loop
                x = 2
            else:
                #ask user to enter correct data if they did not
                print("Please enter a positive integer.")
        except:
            #ask user to enter correct data if they did not
            print("Please enter a positive integer.")

    while x == 2:
        #ask for the value to assign to height
        h = input("What is your height? (m): ")
        try:
            #test if float integer was entered
            h = float(h)
            #test if entered integer is positive integer
            if h >= 0:
                #raise x value to end loop
                x = 3
            else:
                #ask user to enter correct data if they did not
                print("Please enter a positive integer.")
        except:
            #ask user to enter correct data if they did not
            print("Please enter a positive integer.")

#if user chooses imperial run this loop
if u == 1:
    while x == 1:
        #ask for the value to assign to a
        w = input("What is your weight? (lbs): ")
        try:
            #test if float integer was entered
            w = float(w)
            #test if entered integer is positive integer
            if w >= 0:
                #raise x value to end loop
                x = 2
            else:
                #ask user to enter correct data if they did not
                print("Please enter a positive integer.")
        except:
            #ask user to enter correct data if they did not
            print("Please enter a positive integer.")

    while x == 2:
        #ask for the value to assign to a
        print("Please enter your height for feet then inches as directed.")
        #ask for height in feet
        h1 = input("Please enter your height in feet: ")
        #ask for height in inches
        h2 = input("Please enter the inches to add to your height in feet: ")
        try:
            #test if float integer was entered
            h1 = float(h1)
            h2 = float(h2)
            #test if entered integer is positive integer
            if h1 >= 0 and h2 >= 0:
                #raise x value to end loop
                x = 3
            else:
                #ask user to enter correct data if they did not
                print("Please enter a positive integer.")
        except:
            #ask user to enter correct data if they did not
            print("Please enter a positive integer.")

#If imperial units were used convert to metric
if u == 1:
    #round height in feet to nearest whole number
    h1 = round(h1,0)
    #convert height in feet and inches to metres
    h = (h1*12+h2)*0.0254
    #convert weight in pounds to kilograms
    w = w*0.45359237

#calculate the BMI using given equation
BMI = w/(h*h)

#print BMI rounded to 2 decimal places
print("Your BMI is:",round(BMI,2))

#test what BMI weight range the use is in a print appropriate response.
if BMI < 18.5:
    #print the users BMI range
    print("You are underweight.")
if 18 <= BMI < 25:
    #print the users BMI range
    print("You are a healthy weight.")
if 25 <= BMI < 30:
    #print the users BMI range
    print("You are overweight.")
if BMI > 30:
    #print the users BMI range
    print("You are obese.")