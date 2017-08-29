
#6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
#  Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475";

# First find the space
posSpace = text.find(" ")

# Create a new string from the old one, starting from the first space
number = text[posSpace:]

# Strip away the spaces
strippedNumber = number.lstrip()

# Convert the str to a float
strippedNumber = float(strippedNumber)
print(strippedNumber)