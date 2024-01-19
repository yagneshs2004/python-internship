import random
import string
al = list(string.ascii_lowercase)
au = list(string.ascii_uppercase)
sc = list(string.punctuation)
di = list(string.digits)
pt=list(string.ascii_lowercase+string.punctuation+string.digits)

a = int(input("Enter the number of passwords to be generated:- "))
b = int(input("Enter the length of the passwords (minimum = 7):- "))

if(b<7):
    b=7
for i in range(a):
    set = ['al', 'sc', 'di']
    password = ''
    password += random.choice(au)
    password += random.choice(al)
    password += random.choice(sc)
    password += random.choice(di)

    for i in range(4,b):
        password += random.choice(pt)
    print(password)

