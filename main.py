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


