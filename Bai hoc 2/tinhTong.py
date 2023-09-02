import sys

def tinhTong(x: int, y:int) -> int:
    return x + y

if (__name__ == "__main__"):
    print(tinhTong(int(sys.argv[1]), int(sys.argv[2]))) 