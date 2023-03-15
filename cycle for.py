number=int(input("Number: "))
sum= int(str(number)[0])+int(str(number)[1])+int(str(number)[2])
print("Sum= ", sum)
umnog= int(str(number)[0])*int(str(number)[1])*int(str(number)[2])
print("Umnogenie= ", umnog)

num = int(input("Введите целое: "))
sum = 0
while (num != 0):
    sum = sum + num % 10
    num = num // 10
print("Сумма цифр числа равна: ", sum)
