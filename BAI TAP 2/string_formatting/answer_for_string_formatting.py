num = [chr(a) for a in range(ord('0'),ord('9')+1)]
x = str(input('Input: '))
for i in x:
    if i not in num:
        print('Input should be a number!')
        exit()
x = int(x)
if x<1:
    print('Input should be over 0!')
    exit()
elif x>49:
    print('Input should be less than 50!')
    exit()
print('Output: ')
for i in range(1,x+1):
    deci = str(i)
    octa = oct(i)
    octa = list(octa)
    octa = ''.join(octa[2:])
    hexa = hex(i)
    hexa = list(hexa)
    hexa = ''.join(hexa[2:])
    bina = bin(i)
    bina = list(bina)
    bina = ''.join(bina[2:])
    print(' '*(2-len(deci))+deci+' '*(7-len(octa))+octa+' '*(7-len(hexa))+hexa+' '*(7-len(bina))+bina)