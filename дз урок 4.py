# 1. Користувач вводить рядок з клавіатури. Порахуйте кількість літер, цифр у рядку.
# Виведіть обидві кількості на екран. (використовувати цикл)

# password = input("Enter password from 5 to 14 symbols: ")
#
# try:
#         print("letters=", (len([ i for i in password if i.isalpha()])))
#         print("digits:", (len([i for i in password if i.isdigit()])))
#
#         if 5 < (len(password)) > 14 :
#             print(password)
#
#         else:
#             print("Wrong number of symbols")
#
# except Exception as error :
#         print(error)




# 2. Користувач вводить з клавіатури рядок та символ для пошуку.
# Порахуйте скільки разів у рядку зустрічається потрібний символ. Отримане число виведіть на екран.

# string = input("Enter string: ")
# symbol = input("Enter a symbol you want to find: ")
#
# try:
#     if symbol in string :
#         print(string.count(symbol))
#
#     else:
#         print("Symbol not found")
#
# except Exception as error :
#     print(error)
#
# print()




# 3. Користувач вводить з клавіатури рядок, слово для пошуку, слово для заміни.
# Зробіть у рядку заміну одного слова на інше. Отриманий рядок на екрані.
#  v1
# string = input("Enter string: ")
# word = input("Enter a word you want to find: ")
# word_old = input("Enter a word you want to replace: ")
# word_new = input("Enter a new word: ")
#
# try:
#     if word in string :
#         print(word)
#
#     else:
#         print("Word not found")
#
# except Exception as error :
#     print(error)
#
# try:
#     if word_old in string :
#         print("word exists")

# v2

# string = input("Enter string: ")
# word = input("Enter a word you want to find: ")
#
# try:
#     if word in string :
#         print("Word found: ", word)
#
#     else:
#         print("Word not found")
#
#
#     while True:
#         try:
#             word_old = input("Enter a word you want to replace: ")
#             word_new = input("Enter a new word: ")
#
#             if word_old in string :
#                 print("word exists")
#                 break
#
#             else:
#                 print("Choose a word you want to replace in string!")
#                 continue
#
#         except ValueError as error:
#             print(error)
#
#     string2 = string.replace(word_old, word_new)
#     print(string2)
#
# except Exception as error :
#     print(error)




# 4. Дано рядок. (зробити зрізи)
# - Спершу виведіть третій символ цього рядка.
# - У другому рядку виведіть передостанній символ цього рядка.
# - У третьому рядку виведіть перші п'ять символів цього рядка.
# - У четвертому рядку виведіть весь рядок, крім двох останніх символів.
# - У п'ятому рядку виведіть усі символи з парними індексами (вважаючи, що індексація починається з 0, тому символи виводяться з першого).
# - У шостому рядку виведіть усі символи з непарними індексами, тобто, починаючи з другого символу рядка.
# - У сьомому рядку виведіть усі символи у зворотному порядку.
# - У восьмому рядку виведіть усі символи рядка через один у зворотному порядку, починаючи з останнього.
# - У дев'ятому рядку виведіть довжину цього рядка.

# sentence= "I like apples"
# print("1 -", sentence[2:3])
# print("2 -", sentence[11:12])
# print("3 -", sentence[0:5])
# print("4 -", sentence[0:11])
# print("5 -", sentence[1:13:2])
# print("6 -", sentence[2:13:2])
# print("7 -", sentence[::-1])
# print("8 -", sentence[::-2])
# print("9 -", (len(sentence)))



