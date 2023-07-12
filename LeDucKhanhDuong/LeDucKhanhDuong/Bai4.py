def InputData():
    print("Nhập 2 số a,b:\n")
    a = float(input("a= "))
    b = float(input("b= "))
    return a,b
def Sum(a,b):
    c = a+b
    return c
def main():
    a,b = InputData()
    c = Sum(a,b)
    print("Tổng(%.1f"%a,",%.1f"%b,") = %.1f"%c)
if __name__ == "_main_":
    main()