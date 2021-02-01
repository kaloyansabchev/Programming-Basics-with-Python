eggs = int(input())

red = 0
orange = 0
blue = 0
green = 0

for egg in range(0, eggs):
    color = input()
    if color == 'red':
        red += 1
    elif color == 'orange':
        orange += 1
    elif color == 'blue':
        blue += 1
    elif color == 'green':
        green += 1
print(f'Red eggs: {red}')
print(f'Orange eggs: {orange}')
print(f'Blue eggs: {blue}')
print(f'Green eggs: {green}')
if red > orange and red > blue and red > green:
    print(f'Max eggs: {red} -> red')
elif orange > red and orange > blue and orange > green:
    print(f'Max eggs: {orange} -> orange')
elif blue > red and blue > orange and blue > green:
    print(f'Max eggs: {blue} -> blue')
elif green > red and green > orange and green > blue:
    print(f'Max eggs: {green} -> green')
