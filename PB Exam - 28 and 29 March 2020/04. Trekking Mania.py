groups = int(input())
# group_members = int(input())

total_people = 0
musala, montblanc, kili, k2, everest = 0, 0, 0, 0, 0
for group in range(1, groups +1):
    group_members = int(input())
    total_people += group_members
    if group_members <= 5:
        destination = "Мусала"
        musala += group_members
    elif 6 <= group_members <= 12:
        destination = "Монблан"
        montblanc += group_members
    elif 13 <= group_members <= 25:
        destination = "Килиманджаро"
        kili += group_members
    elif 26 <= group_members <= 40:
        destination = "К2"
        k2 += group_members
    else:
        destination = "Еверест"
        everest += group_members

musala_perc = musala / total_people * 100
montblanc_perc = montblanc / total_people * 100
kili_perc = kili / total_people * 100
k2_perc = k2 / total_people * 100
ecerest_perc = everest / total_people *100

print(f"{musala_perc:.2f}%")
print(f"{montblanc_perc:.2f}%")
print(f"{kili_perc:.2f}%")
print(f"{k2_perc:.2f}%")
print(f"{ecerest_perc:.2f}%")

