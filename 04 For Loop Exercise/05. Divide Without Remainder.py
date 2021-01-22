n = int(input())

p1 = 0
p2 = 0
p3 = 0

for num in range(1, n+1):
    number = int(input())
    if number % 2 == 0:
        p1 += 1
    if number % 3 == 0:
        p2 += 1
    if number % 4 == 0:
        p3 += 1

print("{:.2%}".format(p1 / n))
print("{:.2%}".format(p2 / n))
print("{:.2%}".format(p3 / n))