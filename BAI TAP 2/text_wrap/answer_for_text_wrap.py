x = str(input("Input string: "))
y = int(input("Input integer: "))
print("Output:")
for i in range(0,len(x)//4+1):
    print(x[:y])
    x = x[y:]