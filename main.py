n = 124
print (n)
n = "s;dlfk"
print(type(n))# команда type указывает переменная какого типа вызывается

n = "s;dlf'spdffd'sdfsdf" # комбинируя ковычки можно писать другие строки внутри строк

# льыдла
# ываыа
# ывааыв  Массовое копирование возможно с командами cntrl+k  => cntrl+c 
#ldkfmsldkf Массовое раскопирование с командами cntrl+k => cntrl+u
a=5
b = 6.34 
c = "sfsdfs"

print (f"{a} - {b} - {c}") # шаблон f - предоставляет возможность распечатки через определенный знак например - как тут

print ("{} - {} - {}" .format(a,b,c)) #.format предоставляет возможность распечатать переменные как необходимо перечислив их в скобках32

print ("Введите что-нибудь: ")
a = input() # для функции ввода используется команда input
print(a)
b = input("Введите что-нибудь теперь здесь: ") # input так же можно использовать таким образом!
print(b)
print (a + b) #здесь питон воспринимает все как строки, и просто склеивает их а не складывает

#Функции приведения типов

c = 5.89
print(c)
print(type(c))
n = int (c) #int отбрасывает дробную часть
print (n)
print(type(n))
c = bool(c) #Переменные можно переназначать 
print(c)
print(type(c))
# Функция round
a = 3.435
b = 6.346
print(round(a*b, 3)) # round- сначала вводиться число (или переменные которые выявляют это число) а после запятой уже вводиться число знаков которое мы хотим оставить

# Числа и сокращенные операции

iter = 2
iter += 3 # сложение iter = iter + 3
iter -= 4 # вычитание
iter *= 5 # умножение
iter /= 5 # деление
iter //=5 # получение целой части от деления
iter %= 5 # остаток от деления
iter **=5 # возведение в степень

# Логические операции

a = 1 < 3 < 5 < 10
print(a)

# Условия в python

username = input("Введите ваше имя: ")
if username == 'Maria':
    print("Goodluck Manya")
elif username == 'Kolya':
    print("Hey hey Kolyan")
elif username == 'Frodya':
    print("Hi Frodya")
else:
    print("Hello" , username)    

# Циклы while and for

n = 423
sum = 0
while n > 0:
    x = n % 10
    sum += x
    n //= 10
print(sum)  

i = 0
while i < 5:
    if i == 3:
        break  # break как аналог return он останавливает все операции и переходит к print(i)
    i+=1
else:
    print('Пожалуй')
    print ('хватит')
print(i)


# Метод флажка

n = int(input())
flag = True
while flag:
    if n % i == 0: # если остаток при делении числа n на i равен 0
        flag = False
        print (i)
    elif i > n//2: # делитель числа не может быть превышать введенное число, деленное на 2 
        print(n)
        flag = False
    i += 1        

