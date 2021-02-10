import sys
kilometers = int(input())
time_of_the_day = input()

taxi = sys.maxsize
bus = sys.maxsize
train = sys.maxsize
price = 0

if time_of_the_day == "day":
    taxi = 0.79
    if kilometers >= 20:
        bus = 0.09
    if kilometers >= 100:
        train = 0.06
elif time_of_the_day == "night":
    taxi = 0.90
    if kilometers >= 20:
        bus = 0.09
    if kilometers >= 100:
        train = 0.06

if taxi < bus and taxi < train:
    price = 0.7 + kilometers * taxi
elif bus < taxi and bus < train:
    price = kilometers * bus
elif train < bus and train < taxi:
    price = kilometers * train

print(f"{price:.2f}")