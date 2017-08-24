# Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values
# and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.

# Use the file name mbox-short.txt as the file name

# fname = raw_input("Enter file name: ")
fname = "mbox-short.txt"
fh = open(fname)


def extractor(s):
    posSpace = s.find(" ")
    number = s[posSpace:].lstrip()
    number = float(number)
    return number
# Create a counter
count = 0
average = 0

for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    num = extractor(line)
    #print(num)
    average = average + num
    count = count + 1

print("Average spam confidence:", average / count)
