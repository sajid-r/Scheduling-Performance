data = [line.split() for line in file('data.txt', 'rU').read().split('\n')]
del data[-1]
for index, item in enumerate(data):
            data[index] = abs(int(item[0])), abs(float(item[1]))
print tuple(data)
