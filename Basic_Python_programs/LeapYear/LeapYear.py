print("Enter the Year : ")
year = int(input())
while year < 1000 or year > 9999:
    print("Please Enter the four Digits ")
    year = int(input())

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(year, " is a leap Year")
else:
    print(year, " is not leap Year")
