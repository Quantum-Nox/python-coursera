
def openfile():
    fname = raw_input("Enter file name: ")
    try:
        fh = open(fname)
    except:
        print("Error opening file", fname)
        quit()
    return fh

def printit(f):
    for line in f:
        print line.upper().rstrip() #Trailing comma to avoid adding a newline at the end of print

fh = openfile()
printit(fh)