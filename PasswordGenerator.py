import random
import string

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")




def passwordgenerator():
    pass
#ask for length of password, as an int


length = int(input("How many characters does your password need to be? "))

#shuffle the characters
random.shuffle(characters)

#make a list to store the characters in for the password
password = []

#use a For loop to access the input in the length variable
for i in range(length): #use the append method to add the characters to the password list
    password.append(random.choice(characters))
#shuffle the password one more time
random.shuffle(password)
#print quotation makers and a .join to form the password together
print("".join(password))


#invoke function
passwordgenerator()
