print("Привет! Меня зовут Алеша Попович.\n"
      "А тебя как?")
str(input())
print("Очень приятно познакомиться.\n"
      "Подскажите, пожалуйста, сколько будет 2+2?")

answer = int(input())
if (answer == 4) :
    print("Страно, а я думал что 5.")
elif (answer == 5) :
    print("Гениально.")
else:
    print("game over!!!")

print("Не верите проверьте:")
x = int(input("Number 1:"))
y = int(input("Number 2:"))

def sum(a,b):
    return a + b +1

print(sum(x,y))