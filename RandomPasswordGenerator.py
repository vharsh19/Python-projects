import random
import string

all_Char=string.ascii_letters+string.digits+string.punctuation

length=int(input("Enter the length of the required password: "))
password=""

#list Comprehension
res_password = "".join(random.choice(all_Char) for i in range(length))
print("The random password generated is: ",res_password)


#Basic Method
'''password=""
    for i in range(length):
        password +=random.choice(all_Char)
    print("The random password generated is: password)'''
