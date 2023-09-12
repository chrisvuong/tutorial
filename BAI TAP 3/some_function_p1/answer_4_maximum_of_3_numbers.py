x = int(input('first number: '))
y = int(input('second number: '))
z = int(input('third number: '))
if x>y:
    if x>z:
        k=x
    else:
        k=z
else:
    if y>z:
        k=y
    else:
        k=z
print('the max number is '+str(k))