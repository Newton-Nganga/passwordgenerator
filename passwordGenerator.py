import random
 
lower = "qwertyuiopasdfghjklzxcvbnm"
upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
numbers = "1234567890"
symbols="!@#$%^&*()_+"

combined = lower + upper + numbers + symbols

password=[]

print('     _____________________________     ')
print('    |                             |    ')
print('    |    PASSWORD GENERATOR       |    ')
print('    |        BY Newton 🥳         |    ')
print('    |_____________________________|    ')

print(' ')

#Password length
try:
    length = int(input("Enter password length? "))
except ValueError:
    print("Defaulting to 16 character password")
    length = 16
    
#Ask for the amount of password to generate
try:
    num = int(input("How many passwords would You want to generate? "))
except ValueError:
    print("Invalid input...using default value of 10 passwords")
    num = 10

for i in range(num):
    x = "".join(random.sample(combined,length))
    password.append(x)
    
    
print("")
for pas in password:
    print(f'👉🏽:   {pas}')

print(' ')
print('     _____________________________     ')
print('    |                             |    ')
print('    |     Thanks for using        |    ')
print('    |    PASSWORD GENERATOR       |    ')
print('    |_____________________________|    ')
