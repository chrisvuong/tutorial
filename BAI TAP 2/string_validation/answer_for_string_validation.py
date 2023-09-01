x = str(input("Input: "))
print("Output: ")
printed = 0
alpha = [chr(a) for a in range(ord('a'),ord('z')+1)]
ALPHA = [chr(a) for a in range(ord('A'),ord('Z')+1)]
digit = [chr(a) for a in range(ord('0'),ord('9')+1)]
print(x.isalnum())
for i in x:
    if i in (alpha or ALPHA):
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