dk = [chr(a) for a in range(ord('1'),ord('9')+1)]
k='e'
while k!='q':
    k='e'
    x=y=0
    choice = int(input("""Select operation.
    1.Add
    2.Subtract
    3.Multiply
    4.Divide
    5.Convert
    Enter choice(1/2/3/4/5): """))
    while x not in dk:
        x = input('add first number: ')
    while y not in dk:
        y = input('add second number: ')
    x=int(x)
    y=int(y)
    if choice==1:
        kq=x+y
    elif choice==2:
        kq=x-y
    elif choice==3:
        kq=x/y
    elif choice==4:
        kq=x*y
    print(kq)
    k=str(input('do you want to continue?(press"q" to quit or "c" to continue): '))
    while k!='q' and k!='c':
        k=str(input('press"q" to quit or "c" to continue: '))