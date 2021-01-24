width = int(input())
lenght = int(input())
hight = int(input())

volume = width * lenght * hight


command = input()
while command != 'Done':
    boxes = int(command)
    volume -= boxes
    if volume <= 0:
        print(f'No more free space! You need {abs(volume)} Cubic meters more.')
        break

    command = input()

if volume > 0:
    print(f"{volume} Cubic meters left.")