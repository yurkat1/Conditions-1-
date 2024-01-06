# 1. Користувач вводить із клавіатури номер дня тижня (1-7).
# Необхідно вивести на екран назви дня тижня. Наприклад, якщо 1, на екрані напис понеділок, 2 — вівторок тощо.


# try:
#     print("Choose day of the week: 1-Mon, 2- Tue, 3-Wen, 4-Thu, 5-Fri, 6-Sat, 7-Sun")
#     user_select = int(input("Enter day of the week: "))
#     match user_select:
#         case 1 :
#             print("Monday")
#         case 2 :
#             print("Tuesday")
#         case 3 :
#             print("Wednesday")
#         case 4 :
#             print("Thursday")
#         case 5 :
#             print("Friday")
#         case 6 :
#             print("Saturday")
#         case 7 :
#             print("Sunday")
#         case _ :
#             print("Enter valid day of the week!")
#
# except Exception as e:
#     print(f"Error: {e}")

# 2. Користувач вводить два числа. Визначити, чи рівні ці числа, і, якщо ні, вивести їх на екран у порядку зростання

# try:
#     number1 = int(input("Enter first number: "))
#     number2 = int(input("Enter second number: "))
#
#     if number1 == number2 :
#         print("Equal numbers")
#     elif number1 > number2 :
#         print(number1)
#     elif number1 < number2 :
#         print(number2)
#
# except ValueError as error :
#     print("Enter numbers only!")
# except Exception as error :
#     print(error)

# 3. Користувач вводить два числа та матем дію: + - * або /
# Залежно від введеної матем дії вивести результат

# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     math_operation = input("Enter a math operation(+,-,*,/): ")
#
#     if math_operation == "+" :
#         print(num1 + num2)
#     elif math_operation == "-" :
#         print (num1 - num2)
#     elif math_operation == "*":
#         print(num1 * num2)
#     elif math_operation == "/":
#         print(num1 // num2)
#     elif math_operation == "/":
#         print(num1 // num2)
#     else:
#         print("Enter a valid symbol")
#
# except ValueError as error :
#     print("Enter numbers only")
# except Exception as error :
#     print("error")
