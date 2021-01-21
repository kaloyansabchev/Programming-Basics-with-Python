month = input()
nights = int(input())

studio_pn = 0
apartment_pn = 0
if month == 'May' or month == 'October':
    studio_pn = 50
    apartment_pn = 65
    if 7 < nights <= 14:
        studio_pn = studio_pn - (studio_pn * 0.05)
    elif nights > 14:
        studio_pn = studio_pn - (studio_pn * 0.3)
        apartment_pn = apartment_pn - (apartment_pn * 0.1)
elif month == 'June' or month == 'September':
    studio_pn = 75.20
    apartment_pn = 68.70
    if nights > 14:
        studio_pn = studio_pn - (studio_pn * 0.2)
        apartment_pn = apartment_pn - (apartment_pn * 0.1)
elif month == 'July' or month == 'August':
    studio_pn = 76
    apartment_pn = 77
    if nights > 14:
        apartment_pn = apartment_pn - (apartment_pn * 0.1)

total_studio = nights * studio_pn
total_apartment = nights * apartment_pn

print(f"Apartment: {total_apartment:.2f} lv.")
print(f"Studio: {total_studio:.2f} lv.")