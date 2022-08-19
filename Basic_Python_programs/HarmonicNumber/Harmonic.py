Harmonic_result = 0
print("Enter the value of  N for nth  Harmonic ")
num = int(input())
while num == 0:
    print("Enter the vaild input")
    num = int(input())

for i in range(1, num):
    Harmonic_result += 1/i


print("The Harmonic number is ", Harmonic_result)
