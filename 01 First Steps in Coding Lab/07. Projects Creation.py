# 7. Изготвяне на проекти
# Напишете програма, която изчислява колко часове ще са необходими на един архитект, за да изготви проектите на
# няколко строителни обекта. Изготвянето на един проект отнема три часа.
# Вход
# От конзолата се четат 2 реда:
#     1. Името на архитекта - текст;
#     2. Брой на проектите - цяло число.

arch_name = input()
projects = int(input())

total_time = projects * 3
print(f"The architect {arch_name} will need {total_time} hours to complete {projects} project/s.")