# num1 = 10
# num2= 20
# num3 = 30
# print( num1 + num2 + num3)
# print(num1 * num2 * num3)
# print()
#
#
#
# # S = (AC · BD)/2
#
# print("S = (AC · BD)/2")
# a = int(input("Enter side A ="))
# b = int(input("Enter side B ="))
# c = int(input("Enter side C ="))
# d = int(input("Enter height D ="))
#
# t =( a * c * b * d)
# s= t // 2
# print(s)





# Урок 2
# При виконанні дз використовувати Git (робити комміти, працювати в develop гілці, для кожного завдання окрема feature/<назва_гілки> гілка з develop гілки, після завершення роботи над завданням - робити merge feature гілки в dev гілку, після виконання всіх завдань зробити merge develop в master)
# 1. Користувач вводить три цифри з клавіатури. Залежно від вибору користувача програма виводить на екран максимум із трьох, мінімум із трьох або середньоарифметичне трьох чисел.

# num1= int(input("Enter first number: "))
# num2= int(input("Enter second number: "))
# num3= int(input("Enter third number: "))
#
# # мінімум із трьох
# if num1 < num2 < num3 :
#     print(num1)
# elif num2 < num3 < num1 :
#     print(num2)
# elif num3 < num2 < num1 :
#     print(num3)
# else:
#     print("All numbers equal")

# максімум із трьох

# if num1 > num2 > num3 :
#     print(num1)
# elif num2 > num3 > num1 :
#     print(num2)
# elif num3 > num2 > num1 :
#     print(num3)
# else:
#     print("All numbers equal")
#
# # середньоарифметичне трьох чисел
#
# mid = (num1 + num2 + num3) // 3
# print(mid)


# 2. Користувач вводить з клавіатури кількість метрів. Залежно від вибору користувача програма переводить метри милі, дюйми або ярди.
# Надіслати посилання на github з проектом


# print("A unit of measurments (1- miles, 2- inches, 3- yards)")
# unit = int(input("Choose a unit of measurments : "))
# meters = float(input("Enter the number of meters : "))
#
# if unit == 1:
#  miles = meters // 1609.34
#  print("Number of miles:" , miles)
#
# if unit == 2:
#
#  inches = meters * 39.37
#  print("Number of inches:" , inches)
#
# if unit == 3:
#
#  yards = meters * 1.09
#  print("Number of inches:" , yards)




















