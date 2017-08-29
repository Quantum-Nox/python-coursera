#Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'.

def emailcount(fh):
    count = 0
    lst = []
    for line in fh:
        line = line.lstrip()
        if not line.startswith("From ") :
            continue
        lst.append(line.split()[1] )
        count = count + 1
    return [lst,count]


fname = "mbox-short.txt"
fh = open(fname)

result = emailcount(fh)
for x in result[0]:
    print(x)
#print(result[0],sep='\n')
print("There were", result[1], "lines in the file with From as the first word")
