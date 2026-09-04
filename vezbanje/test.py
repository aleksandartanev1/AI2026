array = [0, 1, 2, 3, 4, 5, 6, 7]
x = array[:2]
y = array[2:]
z = array[2:6]
w = array[-1]
u = array[:-1]
r = array[-1:]
print(f"X: {x}")
print(f"Y: {y}")
print(f"Z: {z}")
print(f"W: {w}")
print(f"U: {u}")
print(f"R: {r}")

i = 3
print(array)

array.remove(array[i])
print(array)