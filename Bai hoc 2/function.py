

def addString(string: str, list:list) -> None:
    list.append(string.upper())
# l1 = []
# [addString(input("enter something: "), l1) for i in range(5)]
# print(l1)
########################################################################

# vuong thien phuc -> Vuong Thien Phuc
def inHoaChuCaiThuong(name: str) -> str:
    names = name.split()
    return " ".join([i[0].upper() + i[1:] for i in names])

# print(inHoaChuCaiThuong(input("Enter name:")))

def addAndPrintOut(num: int, max: int) -> int:
    num += 1
    print(num)
    if (num == max):
        return num
    addAndPrintOut(num, max)

# addAndPrintOut(5, 10)



