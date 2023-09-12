dk = [chr(a) for a in range(ord('a'),ord('z')+1)]+[' ']
x = input("Input: ")
while len(x)<1:
    print("Enter your name!")
    x = input("Input: ")
for i in x:
    if i not in dk:
        print('Input should be consists of alphanumeric characters and spaces!')
        exit()
print("Output:")
x = x.split()
for i in range(0,len(x)):
    k = x[i]
    k = k[0].upper()+k[1:]
    x[i] = k
print(' '.join(x))