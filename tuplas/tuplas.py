"""
t0 = 1, 2, 3
t1 = 4, 5, 6
t2 = t0 + t1

print(t0)
print(t1)
print(t2)
"""

t1 = 1, 2, 3, 4, 5
t1 = list(t1)

t1[1] = 20
print(t1)

t1 = tuple(t1)
print(t1)