min_control = int(input())
sec_control = int(input())
distance = float(input())
sec_for_100 = int(input())

control_in_sec = (min_control * 60) + sec_control
reduction = distance / 120
total_reduction = reduction * 2.5
marin_time = (distance / 100) * sec_for_100 - total_reduction

if control_in_sec >= marin_time:
    print(f'Marin Bangiev won an Olympic quota!')
    print(f'His time is {marin_time:.3f}.')
else:
    time_need = control_in_sec - marin_time
    print(f'No, Marin failed! He was {abs(time_need):.3f} second slower.')