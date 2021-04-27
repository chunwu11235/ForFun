
a = [i for i in range(10)]
b = a # reference
assert a is b

c = a[:] # deep copy
assert c is not a
assert c == a

a[2:3] = list("something")
assert b == a
print(a)
print(b)

print(c)

#stride
n = [i for i in range(10)]
print(n[::2])
print(n[::-1])
print(n[3:7:3])
print(n[-3:1:1])
print(n[-3:1:-1])

n1 = n[::-1]
n1[0] = "test"
print(n1)
print(n)

# catch-all unpacking (*)
zero, *m, nine = tuple(n)
print(zero, m, nine)
first, second, *others = n
print(first, second, others)
# *all = n # error

