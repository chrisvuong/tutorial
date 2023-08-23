x = str(input("Input: "))
print("Output: ")
printed = 0
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ALPHA = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
digit = ['1','2','3','4','5','6','7','8','9']
print(x.isalnum())
for i in x:
    if i in alpha or ALPHA:
        print("True")
        printed=1
        break
if printed==0:
    print("False")
printed=0   
for i in x:
    if i in digit:
        print("True")
        printed=1
        break
if printed==0:
    print("False")
printed=0  
for i in x:
    if i in alpha:
        print("True")
        printed=1
        break
if printed==0:
    print("False")
printed=0  
for i in x:
    if i in ALPHA:
        print("True")
        printed=1
        break
if printed==0:
    print("False")
printed=0  