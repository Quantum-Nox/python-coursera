import re

hand = open('actual_data')
total = 0
for line in hand:
    line = line.rstrip()
    store = []
    x = re.findall('[\d]*\d+', line)
    if len(x) > 0:
        x = [int(i) for i in x]  # Obtain the values
        intermediate_sum = sum(x)  # Sum over the values in the line
        total = total + intermediate_sum

print(total)
