import math
kozunaci = int(input())

flour_needed = 0
sugar_needed = 0
moust_flour = 0
moust_sugar = 0

for kozunak in range(0, kozunaci):
    sugar = int(input())
    flour = int(input())
    sugar_needed += sugar
    flour_needed += flour
    if sugar > moust_sugar:
        moust_sugar = sugar
    if flour > moust_flour:
        moust_flour = flour

flour_packeges = flour_needed / 750
sugar_packeges = sugar_needed / 950

print(f"Sugar: {math.ceil(sugar_packeges)}")
print(f"Flour: {math.ceil(flour_packeges)}")
print(f"Max used flour is {moust_flour} grams, max used sugar is {moust_sugar} grams.")