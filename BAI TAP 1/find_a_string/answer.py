string = str(input("write your string: "))
count_char = str(input("write characters need to count: "))
leng = len(count_char)
count = 0
x = 0
for i in range(0,len(string)-leng+1):
   if string[x:leng]==count_char:
     count += 1
   leng += 1
   x += 1
print("out put:",count)