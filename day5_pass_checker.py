#Password Strength Checker

password = (input("Enter your password : "))

spl_character = "!@#$%^&*<.,>/?;:{[}-_=+`~]"

length = len(password)
has_upper = False
has_lower = False
has_digit = False
has_splcharacter = False

for ch in password :
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    elif ch in spl_character:
        has_splcharacter = True

score = 0

if length > 8:
    score +=1
if has_upper :
    score +=1
if has_lower:
    score +=1
if has_digit:
    score +=1
if has_splcharacter:
    score +=1

print("\nPassword Strength Analyzing")
print(f"Length = {length}")
print(f"Uppercase = {has_upper}")
print(f"Lowercase = {has_lower}")
print(f"Digit = {has_digit}")
print(f"your score is {score}")

if score <= 2 :
    print("Your password is weak")
elif score <= 4 :
    print("Your password is Medium")
else :
    print("Your password is strong")
