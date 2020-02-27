#! python3

# Robert Propheter
# Phone and Email Scrapper

'''
This program is designed to scrape your computer's clipboard for phone and email 
addresses. You can also import a file like a Microsoft Word document to scrape. 
If you decide to imoprt a file, you will have to uncomment the file import 
statements starting at line 40. You will also have to comment out line 38 to 
make sure the program is reading the file and not the clipboard.
'''

import pyperclip, re

# Creating a regular expression object for phone numbers 

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # separator
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )''', re.VERBOSE)

# Creating a regular expression object for email addresses

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+         # username
    @                         # @ symbol
    [a-zA-Z0-9.-]+            # domain name
    (\.[a-zA-Z]{2,4}){1,2}    # dot-something
    )''', re.VERBOSE)

# Get the text off the clipboard OR import file

text = str(pyperclip.paste())
'''
file = open("SOME_FILE.txt", "r")     * Use this code for files and the
text = file.readlines()                 above code for copy/paste/clipboard
file.close()
'''

# Extract the email/phone from this text

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy the extracted email/phone to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
