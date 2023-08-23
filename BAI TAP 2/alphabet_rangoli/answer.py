alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
x = y = int(input('Input(integer): '))
if x > 26:
    print("Input no more than 26!")
    exit()
print("Output:")
while x > 0:
    x-=1
    i = alpha[x]
    while y > 0:
            