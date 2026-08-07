import string

print("Password checker")

upper = False
lower = False
digit = False
punc = False

password = input("Enter a password: ")

for pw in password:
    if pw.isupper():
        upper = True
    if pw.islower():
        lower = True
    if pw.isdigit():
        digit = True
    if pw in string.punctuation:
        punc = True

# Check missing requirements
if not upper:
    print("Enter at least 1 uppercase letter")

if not lower:
    print("Enter at least 1 lowercase letter")

if not digit:
    print("Enter at least 1 digit")

if not punc:
    print("Enter at least 1 special character")

# Length check
passlen = len(password)

if upper and lower and digit and punc and passlen >= 8:
    print("Strong Password. Password Accepted!")
else:
    print("Weak Password")