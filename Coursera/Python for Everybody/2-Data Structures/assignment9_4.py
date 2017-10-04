## Python for Everybody Coursera
## Assignment 9_4
## Gustavo Simas da Silva - 2017
## Python Data Structures, Dictionaries

#use mbox-short.txt as filename
name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"

fh = open(name)

all_emails = list()
mail_count = dict()

#iterates through lines of the file and collects all emails
for line in fh:
    if 'From ' in line:
        all_emails.append(line.split()[1])

#iterates through each email and creates dictionary with ocurrences count
for email in all_emails:
    mail_count[email] = mail_count.get(email,0) + 1

max_mail = None
max_count = None

#iterates through keys and values of dictionary and searches for greatest occurrence
for key,value in mail_count.items():
    if max_count is None or value > max_count:
        max_mail = key
        max_count = value

#prints the result
print(max_mail,max_count)
