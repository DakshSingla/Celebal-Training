word= input("enter your password: ")
if(len(word)>=8 and any(char.isupper() for char in word) and any(char.isdigit() for char in word)):
    print("Strong")
else:
    print("week")