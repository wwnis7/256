# What is the password? 12345
# I don't know you.
# Or
# What is the password? abc$123
# Welcome!

username=input("ID:")
password=input("password:")

if password is "abcde":
    print("welcome!")
else:
    print("i don't know you.")


#왜 비번a로 할떈 되는데 abcde로 하면 안될까?