print("Enter the Number")
Number = int(input())
print("prime Factors for are ", Number)
for i in range(2, Number):
    if Number % i == 0:
        print(i)
