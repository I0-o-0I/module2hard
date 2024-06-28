n = int(input('Число от 3 до 20:'))
password = []
for i in range (1,21):
    for j in range (i+1, 21):
        if n % (i + j) == 0:
            password.append(i)
            password.append(j)
print('Пароль:', password)


