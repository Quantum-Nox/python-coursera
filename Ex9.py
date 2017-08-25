#Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail
# messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
#  The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum
# loop to find the most prolific committer.

def emailcount(fh):
    lst = []
    for line in fh:
        line = line.lstrip()
        if not line.startswith("From ") :
            continue
        lst.append(line.split()[1] )
    return lst



def countingSenders(emails):
    d = dict()
    for email in emails:
        d[email] = d.get(email,0) + 1
    return d


fname = "mbox-short.txt"
fh = open(fname)

email_list = emailcount(fh)

email_dict = countingSenders(email_list)

maxi = max(email_dict, key=email_dict.get)

print(email_dict)
print(maxi, email_dict.get(maxi,1))

