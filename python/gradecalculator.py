m=int(input("enter marks in maths :"))
p=int(input("enter marks in physics :"))
c=int(input("enter marks in chemistry :"))

total=(m+p+c)
Average=(m+p+c)/3
percentage=(total/300)*100
Grade=""
if percentage >=90:
    Grade="A"
elif percentage >=80 and percentage < 90:
    Grade="B"
elif percentage >=60 and percentage < 80:
    Grade="C"
else:
    Grade="F"

print(f"Total marks is : {total}\nAverage marks is : {Average}\nGrade is : {Grade}")
