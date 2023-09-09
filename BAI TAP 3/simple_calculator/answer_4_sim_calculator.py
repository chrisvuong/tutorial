k='e'
while k!='q':
    choice = int(input("""Select operation.
    1.Add
    2.Subtract
    3.Multiply
    4.Divide
    5.Convert
    Enter choice(1/2/3/4/5): """))
    x = int(input('add first number: '))
    y = int(input('add second number: '))
    if choice==1:
        kq=x+y
    elif choice==2:
        kq=x-y
    elif choice==3:
        kq=x/y
    elif choice==4:
        kq=x*y
    else:
        quit()
    print(kq)
    k=str(input('do you want to continue?(press"q" to quit or "c" to continue): '))