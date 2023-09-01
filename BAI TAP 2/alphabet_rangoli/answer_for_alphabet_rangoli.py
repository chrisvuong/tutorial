num = [chr(a) for a in range(ord('0'),ord('9')+1)]
alpha = [chr(a) for a in range(ord('a'),ord('z')+1)]
x = str(input('Input(integer): '))
for i in x:
    if i not in num:
        print('Input need to be a number!') 
        exit()
x = int(x)
if x>26:
    print("Input need to be less than 26!")
    exit()
if x<1:
    print("Input need to be more than 0!")
    exit()
print("Output:")
for i in range(0,x):
    if i!=0:
        k = '-'.join(alpha[:i])+'-'+'-'.join(alpha[i::-1])
    else:
        k = alpha[0]
    l=((2*x-1)*2-1-len(k))//2
    print('-'*l+k+'-'*l)
for i in range(x-2,-1,-1):
    if i!=0:
        k = '-'.join(alpha[:i])+'-'+'-'.join(alpha[i::-1])
    else:
        k = alpha[0]
    l=((2*x-1)*2-1-len(k))//2
    print('-'*l+k+'-'*l)