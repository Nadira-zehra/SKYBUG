import random
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols=['@','!','#','$','%','*','(',')']
digits=['0','1','2','3','4','5','6','7','8','9']
print("Welcome to the password Generator!")
letters=int(input("How many alphabets you want to like in password\n"))
symbol=int(input("How many symbols you want to like in passord\n"))
numbers=int(input("How many digits you want to like in passord\n"))
password=""
for i in range(1,letters+1):
    char=random.choice(alphabets)
    password+=char
for i in range(1,symbol+1):
    char=random.choice(symbols)
    password+=char
for i in range(1,numbers+1):
    char=random.choice(digits)
    password+=char
print("Print the generated password on the screen")
print(password)
