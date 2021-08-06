n = input()

for i in range(len(n)):
    for j in range(i+1, len(n)):
        if (n[i] == n[j]):
            print("Есть одинаковые")
            quit()
print("Все элементы уникальны")