########  Loops II & Functions  #########
hundry=True
satisy=0
while satisy <=10:
    satisy +=1
    print('Give me something to eat!!')
else:
    print('I am super satisfied now')
    
'''Quick Coding Exercise
Let's find the duplicate emails in a list of emails and print them.'''

email_list = ['roger@hey.com','michael@hey.com','roger@hey.com','prince@gmail.com']
duplicate_email=[]
for email in email_list:
    if email_list.count(email) > 1 and email not in duplicate_email:
        duplicate_email.append(email)
print(duplicate_email)
    

    