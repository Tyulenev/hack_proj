
#import requests

i=0

email_user_t = "AbraKadabra@gmail.com"
name_user_t = "Alex"
sername_user_t = "Ivanov"
date_birth_t = "08.08.1980"

#generate list alph
list_alphabet = []

#remove end of email
mail1 = email_user_t.split("@")

#split birthday
birt1 = date_birth_t.split(".") #need add another char "/", "," and etc.

#Add to list
list_alphabet.append(mail1[0])
list_alphabet.append(name_user_t)
list_alphabet.append(sername_user_t)
for d1 in birt1:
    list_alphabet.append(d1)

print (list_alphabet)
base = len(list_alphabet)
i = 0
length = 1
#passList = []

while True:
    # i: 10 -> base

    password = ''
    temp = i
    rest = 0
    count_of_pass_parts = 0
    while temp != 0:
        rest = temp % base
        temp = temp // base
        count_of_pass_parts += 1


        password = list_alphabet.__getitem__(rest) + password

    password = list_alphabet.__getitem__(0) * (length - count_of_pass_parts) + password
    print(length, i, password)

    #response = requests.post('http://127.0.0.1:4000/auth',
    #                         json={'login': 'cat', 'password': password})
    #if response.status_code == 200:
    #    print('Success!')
    #    break

    if password == list_alphabet.__getitem__(-1) * length:
        #i = base*length
        i=0
        length += 1

    else:
        i += 1


    if length>base: #May be changed
        print("All combinations is here")
        break

def delete_end_email(self, mail_in:str):
    mail_out = ''
    return int(mail_in.find("@"))


