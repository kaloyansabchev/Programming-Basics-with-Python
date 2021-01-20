# 3. Клас животно
# Напишете програма, която отпечатва класа на животното според неговото име, въведено от потребителя.
#     1. dog -> mammal
#     2. crocodile, tortoise, snake -> reptile
#     3. others -> unknown

a = input()

if a == 'dog':
    print('mammal')
elif a == 'crocodile' or a == 'tortoise' or a == 'snake':
    print('reptile')
else:
    print('unknown')