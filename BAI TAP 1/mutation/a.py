string = str(input("write your string(string): "))
num = int(input("character position(integer): "))
rep_char = str(input("replace character(string): "))
num -= 1
x = list(string)
x[num] = rep_char
print(''.join(x))