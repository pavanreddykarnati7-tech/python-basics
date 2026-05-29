

# using temp variables
"""a=int(input("enter a value:"))
b=int(input("enter a value:"))
temp=a
a=b
b=temp
print("After swapping :"
      "value of a:",a,
       "value of b:",b)"""

# without using temp variables
a=int(input("enter a value:"))
b=int(input("enter a value:"))
a+=b
b=a-b
a=a-b
print("value of a :",a)
print(f"value of b:{b}")
