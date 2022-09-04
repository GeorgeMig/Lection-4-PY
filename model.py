x = 0
y = 0

def init (a, b):
    global x ## команда глобал присваивает значение переменной вне метода
    global y
    x = a
    y = b

init (11, 22)

print(x)
print(y)