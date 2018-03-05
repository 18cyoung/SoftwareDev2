f = open("weather.txt", 'r')
t = open("summary.txt", 'a')

def avTemp(dew):
    if dew <= 16.0:
        print("dry and comfortable")
    elif 16.0 < dew < 20.0:
        print("muggy")
    elif dew >= 20.0:
        print("very sticky and oppressive")
    return(avTemp)

# make a list for each value
daylist = []
datelist = []
dewlist = []
listTotal = []

x = 0

for Line in f:
    #strip new line character
    Line = Line.strip('\n')
    #turn line into a list split at each space
    Line = Line.split(' ')
    #make a list by popping the needed value from line and appending into a new list
    day = Line.pop(0)
    date = Line.pop(0)
    dew = Line.pop(0)
    daylist.append(day)
    datelist.append(date)
    dewlist.append(dew)
    #find max and min temps using the max and min function for the line
    maxTemp = max(Line)
    minTemp = min(Line)
    dailyTemps = Line

#print out the needed data per day by increasing the x value, which is the positions on the related list
while x != 100:
    #try each print, if the index becomes to high, exit while loop.
    try:
        print("daylist" , daylist[x])
        print("datelist" , datelist[x])
        print("dewlist" , dewlist[x])
        print("dailyTemps" , dailyTemps)
        print("maxtemp" , maxTemp)
        print("mintemp" , minTemp)
        av = avTemp(float(dew[0]))
        print(av)
        print("---")
        x = x + 1
    except (IndexError):
        x = 100

#change all the lists into strings as they were given, seperated by spaces
day = ' '.join(daylist)
date = ' '.join(datelist)
dew = ' '.join(dewlist)
max = ' '.join(maxTemp)
min = ' '.join(minTemp)


#write all the needed data in the summary.txt file
t.write(day)
t.write("\n")
t.write(date)
t.write("\n")
t.write(dew)
t.write("\n")
t.write(max)
t.write("\n")
t.write(min)
t.write("\n")
#t.write(av)
t.write("\n")

#close file
f.close()
t.close()



