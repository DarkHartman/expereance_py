
year = int(input("Введите год для проверки:"))
if (year >= 1900 and year < 1000000):
    print()
else:
    exit(print("the entered year does not meet the conditions"))

a = int(year)
if(a%4 == 0 and a%100 == 0 and a%400 == 0):
    print(year,"is leap year")
elif(a%4 == 0 and a%100 == 0 and a%400 != 0):
    print(year,"is not leap year")
elif(a%4==0 and a%100 != 0 and a%400 != 0):
    print(year,"is leap year")
else:
    print(year,"is not leap year")
