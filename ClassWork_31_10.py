# 1.  Роздрукувати всі парні числа менші 100 
# (написати два варіанти коду: один використовуючи цикл while, а інший з використанням циклу for).

a = 0
while a<100:
    if a % 2 == 0:
        print(a) 
    a = a+1 

# 2.  Роздрукувати всі непарні числа менші 100. 
# (написати два варіанти коду: один використовуючи оператор continue, а інший без цього оператора).

for item in range(1,100,2):
    print(item)

# 3.  Перевірити чи список містить непарні числа.
#           (Підказка: використати оператор break)

for element in [2,3,4,5,6,7]:
    if element % 2 != 0:
        break
    print(element)
print("The end.")


# 4.  Створити список, який містить елементи цілочисельного типу, 
# потім за допомогою циклу перебору змінити тип даних елементів на числа з плаваючою крапкою. 
# (Підказка: використати вбудовану функцію float ()).

todo = [1,2,3,4,5,6,7]
i = 0
while i<len(todo):
    todo[i] = float(todo[i])
    i=i+1
print(todo)

# 5.  Вивести числа Фібоначі включно до введеного числа n, використовуючи цикли. 
# (Послідовність чисел Фібоначі 0, 1, 1, 2, 3, 5, 8, 13 і т.д.)
#                                     1  2  3  4    
fib_1 = 0
fib_2 = 1

n = input("Enter number ")
n = int(n)
print(int(fib_1))
print(int(fib_2))
while fib_2 < n:
    tmp = fib_2
    fib_2 = fib_1 + fib_2
    fib_1 = tmp
    print(fib_2)
    

# 6.  Створити список, що складається з чотирьох елементів типу string. 
# Потім, за допомогою циклу for, вивести елементи по черзі на екран.

created_list = ["Winter", "Spring", "Summer", "Autumn"]
for element in range(len(created_list)):
    print(created_list[element])

# 7.  Змінити попередню програму так, щоб в кінці кожної букви елементів при виводі 
# додавався певний символ, наприклад “#”. 
#           (Підказка: цикл for може бути вкладений в інший цикл, 
#            а також  треба використати функцію print(“ ”, end=”%”)).

created_list = ["Winter", "Spring", "Summer", "Autumn"]
for element in created_list:
    for item in element:
        print(item, end="%")
    print()
    
    