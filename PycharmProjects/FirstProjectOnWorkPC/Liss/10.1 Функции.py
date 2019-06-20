add = lambda x, y: x * y
print(add(2, 5))
print(add('q', 5))


print((lambda q, w: q * w)(2, 6))

fun = lambda *args: args
print(fun(2, 56, 78.56))