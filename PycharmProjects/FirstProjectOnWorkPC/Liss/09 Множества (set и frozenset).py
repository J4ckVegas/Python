a= set ("hello")
print(type(a))
print(a)

b = {i ** 2 for i in range(10)}
print(type(b))
print(b)

c = set ("Hello")
d = frozenset ("Qwerty")
a.add (1)
print(c)
print(d)

e = ['r', 's', 'w', 'a', 's', 'w']
print(e)
print(set (e))

f = {32, 45, 43.23, 76}
x = 45
print(len (f))
print(x in f)

g = {32, 45, 43.23, 76}
y = {67, 12, 90}
print(g.isdisjoint(y))
print(g == y)

k = {32, 45, 43.23, 76}
n = {67, 12, 90, 45, 32}
k.intersection_update(n)
print(k)

p = {32, 45, 43.23, 76}
o = {67, 12, 90, 45, 32}
p.difference_update(o)
print(p)

w = {32, 45, 43.23, 76}
q = {67, 12, 90, 45, 32}
w.symmetric_difference_update(q)
print(w)