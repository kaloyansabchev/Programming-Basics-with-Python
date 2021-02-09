# Басейн с обем V има две тръби от които се пълни. Всяка тръба има определен дебит (литрите вода минаващи през една тръба за един час).
# Работникът пуска тръбите едновременно и излиза за N часа. Напишете програма, която изкарва състоянието на басейна, в момента, когато работникът се върне.
volume = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

p1_v = p1 * h
p2_v = p2 * h
total_v = p1_v + p2_v

if total_v < volume:
    to_full = total_v / volume
    percentage_p1 = p1_v / total_v
    percentage_p2 = p2_v / total_v

    print("The pool is " + "{:.2%}".format(to_full) + " full.")
    print("Pipe 1: " + "{:.2%}".format(percentage_p1) + ".")
    print("Pipe 2: " + "{:.2%}".format(percentage_p2) + ".")
else:
    overflow = total_v - volume
    print(f"For {h} hours the pool overflows with {overflow:.2f} liters.")