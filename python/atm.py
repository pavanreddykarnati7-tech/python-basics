n=input("insert the card :")

if n=="yes":
    print("enter the pin")
    pin=int(input())
    print("enter the amount")
    amount=int(input())
    print("transaction successful")

elif n=="no":
    print("card is not inserted")
else :
    print("invalid input")
