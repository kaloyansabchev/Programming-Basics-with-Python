name = input()
seasons = int(input())
n_seasons = int(input())
duration = float(input())

one_episod = duration * 0.2
one_episod_and_ads = duration + one_episod
special_episod = seasons * 10
total_time = one_episod_and_ads * n_seasons * seasons + special_episod
print(f"Total time needed to watch the {name} series is {round(total_time)} minutes.")