# 5. Познай паролата
# Да се напише програма, която чете парола (един ред с произволен текст), въведена от потребителя и проверява дали въведеното
# съвпада с фразата "s3cr3t!P@ssw0rd". При съвпадение да се изведе "Welcome". При несъвпадение да се изведе "Wrong password!".

password = input()

if password != 's3cr3t!P@ssw0rd':
    print("Wrong password!")
else:
    print("Welcome")