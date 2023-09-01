x = int(input("Input X: "))
y = int(input("Input Y: "))
if x>=y or x*3!=y:
    print("X must be lower than Y three times!")
    exit()
elif x%2==0 or y%2==0:
    print("X and Y should be odd numbers!")
    exit()
for i in range(0,(x-1)//2):
    if i==0:
        k = '.|.'
    else:
        k = '.|.'*i*2+'.|.'
    l = (3*x-len(k))//2
    print('-'*l+k+'-'*l)
l = (3*x-7)//2
print('-'*l+'WELCOME'+'-'*l)
for i in range((x-1)//2-1,-1,-1):
    if i==0:
        k = '.|.'
    else:
        k = '.|.'*i*2+'.|.'
    l = (3*x-len(k))//2
    print('-'*l+k+'-'*l)