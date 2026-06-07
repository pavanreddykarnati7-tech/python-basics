a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
def swap(a,b):
    a+=b
    b=a-b
    a=a-b
    print("After swapping: a =", a, "b =", b)
swap(a, b)