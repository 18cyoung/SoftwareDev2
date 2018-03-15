fname = input("Which file do you wish to open?: ")
wname = input("Which file do you wish to write to?: ")
f = open(fname, 'r')
t = open(wname, 'a')

def getProfit(SellAmount,C,average):
    P = average*(SellAmount-C)
    print(P)
    return getProfit

def Vintage(SumTotal):
    if SumTotal > 100:
        print("The vintage was excellent")
    elif 40 <= Sumtotal <= 100:
        print("The vintage was good")
    elif SumTotal < 40:
        print("The vintage was poor")
    return Vintage

C = int(input("What is the cost price per tonne? (in dollars): "))

vlist = []
listTotal = []

for line in f:
    #strip new line character
    line = line.strip('\n')
    line = line.split(' ')
    vname = line.pop(0)
    vlist.append(vname)

    total = 0
    for i in line:
        total += float(i)
    listTotal.append(total)
print(vlist)
print(listTotal)

#close file
f.close()
t.close()

average = float((sum(listTotal))/(len(listTotal)))
print(round(average,2))

SumTotal = sum(listTotal)

#newlist = listTotal.sort()
lowest = min(listTotal)
print(lowest)

highest = max(listTotal)
print(highest)

SellAmount = sum(listTotal)*(45/100)
print(SellAmount)

getProfit(SellAmount,C,average)

Vintage(SumTotal)

