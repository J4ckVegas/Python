def decoratpr (func):
    def wrapper ():
        print("Код до выполнения функции")
        func()
        print("Код, который сработал после функции")
    return wrapper

def show ():
    print("Я обычная функция")

show()
dec = decoratpr(show)
dec()
