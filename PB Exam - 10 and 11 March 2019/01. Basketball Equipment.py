fee = int(input())

boots = fee - (fee * 0.4)
suit = boots - (boots * 0.2)
balls = suit / 4
accses = balls / 5
total = fee + boots + suit + balls + accses
print(f'{total:.2f}')