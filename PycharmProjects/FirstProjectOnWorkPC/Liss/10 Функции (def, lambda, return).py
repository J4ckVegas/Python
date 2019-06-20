def func (x):
    def add (a):
        return x + a
    return add

test = func(100)
print(test(200))


def func2 ():
    q = 5
    w = 10
    e = 25
    pass
print(func2())


def func3 (r, u, o = 2):
    res = r + u
    res *= o
    return res
print(func3(2, 4))

def func4 (*args):
    return args
print(func4(2, 'dfs', 3.23))

def func5 (**argss):
    return argss
print(func5(aa=23, bb=34, cc=87))