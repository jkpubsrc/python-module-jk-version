#!/usr/bin/python3




from jk_version import *




v = Version.now()
assert v.isDateBase
print("v:", v)

v2 = Version.now()
assert v2.isDateBase
print("v2:", v2)


vnumbers = v.numbers
print("v:", vnumbers)

v3 = Version(vnumbers + [ 1 ])
assert v3.isDateBase
print("v3:", v3)

assert v3 > v
assert v.length == 4
assert v3.length == 5

v3numbers = v3.numbers[0:4]
assert vnumbers == v3numbers

v4numbers = list(v3.numbers)
v4numbers[-1] += 1
v4 = Version(v4numbers)
print("v4:", v4)

assert v4 > v3




