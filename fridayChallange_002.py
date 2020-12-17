'''
Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9.
Сумма этих чисел равна 23.
Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
'''


sum = 0
steps = 0
rng = 1000  #desired range
n3 = 3      #number 1
n5 = 5      #number 2

for i in range(rng):
    if not i%n3 or not i%n5:
        sum += i
        steps += 1

print ("Sum of integer numbers in range of", rng, "which fully divide by",n3, "and", n5, "is equal to", sum)
print ("Number of steps", steps)
