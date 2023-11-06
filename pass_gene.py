#IMPORTING NEEDED FUNCTION FOR OPERATIONS;
import random
import string
#WELCOME MESSAGE
print('HELLO CODSOFT WELCOME TO PASSWORD GENERATOR!!')
#GETTING LENGTH.
length = int(input('\nEnter the length of password: '))
#USING STRING FUNCTION(METHOD)
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
#MERGING
all = lower + upper + num + symbols
temp = random.sample(all,length)
password = "".join(temp)
#RESULT
print(password)

