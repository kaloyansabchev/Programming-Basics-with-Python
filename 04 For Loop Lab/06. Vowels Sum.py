word = input()
a = 0
e = 0
i = 0
o = 0
u = 0

(" ".join(word))

for char in word:
    if char == "a":
        a += 1
    elif char == "e":
        e += 2
    elif char == "i":
        i += 3
    elif char == "o":
        o += 4
    elif char == "u":
        u += 5
print(a + e + i + o + u)
