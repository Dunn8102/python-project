import math
def InputData():
    a=float(input("Nhap a: "))
    b=float(input("Nhap b: "))
    c=float(input("Nhap c: "))
    return a,b,c
def GiaiPT(a,b,c):
    if (a == 0):
        if (b == 0):
            print ("Phương trình vô nghiệm!")
        else:
            print ("Phương trình có một nghiệm: x = ", + (-c / b))
        return
    delta = b**2 - 4 * a * c
    if delta < 0 :
        print("phuong trinh vo nghiem ")
    if delta ==0:
        x=(-b)/(2*a)
        print("Ngiem x1=x2=", x, end = '\n')
    else:
        x1 = (float)((-b + math.sqrt(delta)) / (2 * a))
        x2 = (float)((-b - math.sqrt(delta)) / (2 * a))
        print ("Phương trình có 2 nghiệm là: x1 = ", x1, " và x2 = ", x2, end = '\n')
def main():
    a,b,c =InputData()
    GiaiPT(a,b,c)
if __name__ == "__main__":
     main()