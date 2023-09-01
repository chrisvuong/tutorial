x = int(input('Input: '))
if x<1:
    print('Input should be over 0!')
    exit()
elif x>49:
    print('Input should be lower than 50!')
    exit()
elif x%2==0:
    print('Input should be an odd number!')
print('Output: ')
for i in range(0,x):
    k = 'H'*i*2+'H'
    l = x-i-1
    print(' '*l+k)
    if i==x-1:
        l = len(' '*l+k)
l = (l-x)//2
j = loop = x//2+1
m = 0
for i in range(0,3*x):
    if loop != 0:
        if i==(x*3-j)//2+m:
            loop -= 1
            m += 1
            k=' '*l+'H'*x*5+' '*l
        else:
            k=' '*l+'H'*x+' '*3*x+'H'*x+' '*l
    else:
        k=' '*l+'H'*x+' '*3*x+'H'*x+' '*l
    print(k)
    if i == 3*x-1:
        l_sp = len(k)-2*l-x
for i in range(x-1,-1,-1):
    k = 'H'*i*2+'H'
    l = x-i-1+l_sp
    print(' '*l+k)