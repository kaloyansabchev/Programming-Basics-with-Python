broi_kozunak = int(input())
kori_egg = int(input())
kg_kurabii = int(input())

# kozunak = 3.2
# egg = 4.35
# kurabii = 5.4
# dye_egg = 0.15

price_kozunak = broi_kozunak * 3.20
price_egg = kori_egg * 4.35
price_kurabii = kg_kurabii * 5.40
price_dye_egg = kori_egg * 12 * 0.15

total = price_kurabii + price_egg + price_dye_egg + price_kozunak
print(f"{total:.2f}")