fname = input("What file do you wish to open? ")
try:
    f = open(fname, "r") # 'r' means read only, 'w' means write only (clears file if file exists), 'a' appends to existing file
except FileNotFoundError:
    print("File does not exist")
    exit(0)

#Prints contents of file
for line in f:
    #strip new line character
    line = line.strip("\n")
    print(line)

#close file
f.close()