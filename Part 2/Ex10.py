#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
#  You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

def emailHourExtractor(fh):
    lst = []
    for line in fh:
        line = line.lstrip()
        if not line.startswith("From "):
            continue
        lst.append(line.split()[5])  #5 to get the time stamp
    return lst

def extractTime(lst):
    hour = []
    for line in lst:
        hour.append(line.split(":")[0])  # zero to get the first entry
    return hour


def countingSenders(emails):
    d = dict()
    for email in emails:
        d[email] = d.get(email, 0) + 1
    return d


fname = "mbox-short.txt"
fh = open(fname)

email_list = emailHourExtractor(fh)  # Obtain the emails
hours = extractTime(email_list)  # Extract the hour
hour_dict = countingSenders(hours)  # Create a dictionary

t = hour_dict.items()
t.sort()

for key, val in t:
    print(key, val)
