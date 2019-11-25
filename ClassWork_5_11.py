# 1.  Створити список цілих чисел, які вводяться з терміналу 
# та визначити серед них максимальне та мінімальне число.

count_user_list = input("Input amount of list values: ")
user_list = []
for element in range(int(count_user_list)):
   user_list.append(int(input("Next number: ")))
print(user_list)
print("Maximum number is ", max(user_list))
print("Minimum number is ", min(user_list))

count_user_list = input("Input amount of list values: ")
user_list = [input("Next namber: ") for values in (range(int(count_user_list)))]
print(user_list)
print("Maximum number is ", max(user_list))
print("Minimum number is ", min(user_list))

# 2.  В інтервалі від 1 до 10 визначити числа 
# •  парні, які діляться на 2,
# •  непарні, які діляться на 3, 
# •  числа, які не діляться на 2 та 3.

for x in range(1, 11):
    if x % 2 == 0:
        print(x, "is even multiple by 2")
    if x % 3 == 0:
        print(x, "is even multiple by 3")
    if x % 2 != 0 and x % 3 != 0:
        print(x, "is not even multiple by 2 and 3")

# 3.  Написати програму, яка обчислює факторіал числа, яке користувач вводить.(не використовувати рекурсивного виклику функції)

fact_num = int(input("Please, enter any number: "))
temp = 1
while fact_num > 1:
    temp *= fact_num
    fact_num -= 1
print("Factorial of entered number is:", temp)

# 4.  Напишіть скрипт, який перевіряє логін, який вводить користувач. 
# Якщо логін вірний (First), то привітайте користувача. 
# Якщо ні, то виведіть повідомлення про помилку. 
# (використайте цикл while)

login_name = input("Please enter your login name: ")
while login_name != "First":
    print("Invalid login name.")
    break
else:
    print("Hello,", login_name)

# 5.  Перший випадок. 
# Написати програму, яка буде зчитувати числа поки не зустріне від’ємне число. 
# При появі від’ємного числа програма зупиняється (якщо зустрічається 0 програма теж зупиняється).

read_num = 1
while read_num >=1:
    read_num = int(input("Please enter any number: "))
    
# 6.  Другий випадок. 
# На початку на вхід подається кількість елементів послідовності, а потім самі елементи. При появі від’ємного числа програма зупиняється 
# (якщо зустрічається 0 програма теж зупиняється).

el_amount = int(input("Input amount of elements: "))
item = 0
while item < el_amount:
        custom_element = int(input("Input digit: "))
        item +=1
        if custom_element <=0:
            print("Stop!")
            break
        else:
            continue

# 7.  Знайти прості числа від 10 до 30, а всі решта чисел представити у вигляді добутку чисел 
# (наприклад 10 equals 2 * 5
#                     11 is a prime number
#                     12 equals 2 * 6
#                     13 is a prime number
#                     14 equals 2 * 7
#                      ………………….)

for element in range(10, 30):
    isPrime = True
    for numb in range(2, element):
        if element % numb == 0:
            isPrime = False
            print(element, "equals", numb, "*", int(element / numb))
            break
    else:
        print(element, "is prime")
           
# 8.  Відсортувати слова в реченні в порядку їх довжини (використати List Comprehensions)

sentence = str(input("Please, input any sentence: "))
sentence = sentence.split(" ")
for word in sentence:
    sentence.sort() and ''.join(sentence)
    print(word)