import random


head = 0
teal = 0
NumberOfFlip = int(input("Enter the number of times you want to flip coin :"))

while NumberOfFlip <= 0:
    print("Invaild input, please a vaild input greater then 0 :")
    NumberOfFlip = int(input("Enter the number of times you want to flip coin :"))


for i in range(NumberOfFlip):
    r1 = random.randint(0, 1)

    if r1 < 0.5:
        head = head + 1
    else:
        teal = teal + 1
head_per = float(head)*100 / NumberOfFlip
teal_per = float(teal)*100/NumberOfFlip
print(head_per)
print(teal_per)
