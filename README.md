# password_generator
A python script that generates strong passwords by default ten 16-character passwords.

## Requirements  
👉: Python3 installed   

## Run the script  
  ```sh
    python passwordGenerator.py
  ```

## Logic
```python
"""

create the following variables

lower ->holds all the lowercasecharacters
upper -> holds all the uppercase characters
numbers -> holds all the numerical characters
symbols -> holds the rest of the symbols||characters

"""
combined = lower + upper + numbers + symbols

password=[]

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

```

## screensnap of the script
![password](https://github.com/Newton-Nganga/passwordgenerator/assets/93589514/b9dae2dd-2d9e-430e-9717-b005d8c7684e)
