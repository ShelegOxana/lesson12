num = int(input("Number: "))
sum = 0
mult = 1
while (num != 0):
    digin = num % 10
    num = num // 10
    sum = sum + digin
    mult = mult * digin
print("Summa: ", sum)
print("Umnogenie: ", mult)