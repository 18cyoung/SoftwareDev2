q = int(input("What is the day of the month? (E.g.1-31): "))
m = int(input("What is the month? (E.g.1-12): "))
k = int(input("What is the year of the century? (E.g.(20'18'): "))
if m == 1 or m == 2:
    m = m+12
    k = k-1
j = int(input("What is the zero based century? (E.g.('20'18): "))

h = int((q+((13*(m+1))/5)+k+(k/4)+(j/4)-2*j) % 7)

if h == 0:
    h="Saturday"
if h == 1:
    h="Sunday"
if h == 2:
    h="Monday"
if h == 3:
    h="Tuesday"
if h == 4:
    h="Wednesday"
if h == 5:
    h="Thursday"
if h == 6:
    h="Friday"


print(h)

# h = day of week
# q is day of month (1-31)
# m is the month (3=march,4=april...14=feb)
#k is the year of century (20"00")
# j is zero based century ("20"00)