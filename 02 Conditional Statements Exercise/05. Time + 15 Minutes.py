# 5. Време + 15 минути
# Да се напише програма, която чете час и минути от 24-часово денонощие, въведени от потребителя и изчислява колко ще е часът след
# 15 минути. Резултатът да се отпечата във формат часове:минути. Часовете винаги са между 0 и 23, а минутите винаги са между 0 и 59.
# Часовете се изписват с една или две цифри. Минутите се изписват винаги с по две цифри, с водеща нула, когато е необходимо.

hours = int(input())
minutes = int(input())

new_minutes = minutes + 15
newest_minutes = 0
newest_hours = 0

if new_minutes >= 60:
    newest_minutes = new_minutes - 60
    newest_hours = hours + 1
    if newest_hours >= 24:
        newest_hours = 0

if new_minutes <= 59:
    newest_minutes = new_minutes
    newest_hours = hours

# if hours < 23 and new_minutes < 59:
#     newest_hours = hours
#     newest_minutes = new_minutes

print(f'{newest_hours}:{newest_minutes:02d}')
