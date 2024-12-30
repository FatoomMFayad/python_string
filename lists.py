x = [2, 5, 8, 10, 55, 11, 9, 88, 100, 101]
y = [99, 0, 33]

print(x)
print(x[1])
print(x[-3:])
print(x[::2])
print(len(x))
print(sorted(x))
print(sorted(x, reverse=True))
print(sum(x))
x.append(102)
print(x)
x.insert(0,1)
print(x)
x.extend(y)
print(x)
last_item = x.pop()
print(x)
