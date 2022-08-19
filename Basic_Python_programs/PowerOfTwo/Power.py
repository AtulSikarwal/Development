print("Enter the number for Power")
pow = int(input())
while pow < 0 or pow >= 31:
    print("Enter the Valid number")
    pow = int(input())
for i in range(1, pow):
    print("Result of Power ", i, "is", 2**i)
