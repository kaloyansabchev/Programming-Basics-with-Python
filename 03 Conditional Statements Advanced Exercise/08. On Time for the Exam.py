exam_start_h = int(input())
exam_start_m = int(input())
arrive_hour = int(input())
arrive_min = int(input())

exam_start_total = exam_start_h * 60 + exam_start_m
arrive_total = arrive_hour * 60 + arrive_min

late = 0
early = 0
on_time = 0

if arrive_total > exam_start_total:
    late += 1
    print('Late')
elif arrive_total < exam_start_total - 30:
    early += 1
    print("Early")
elif arrive_total <= exam_start_total:
    on_time += 1
    print("On time")

end_time = exam_start_total - arrive_total
end_time = abs(end_time)
if late != 0:
    end_time_m = 0
    if end_time >= 60:
        end_time_m = end_time // 60
        end_min = end_time - (end_time_m * 60)
        if end_min < 10:
            print(f"{abs(end_time_m)}:0{end_min} hours after the start")
        else:
            print(f"{abs(end_time_m)}:{end_min} hours after the start")
        quit()
    end_time_m = abs(end_time)
    print(f"{abs(end_time_m)} minutes after the start")
if early != 0:
    if end_time >= 60:
        end_time_m = end_time // 60
        end_min = end_time - (end_time_m * 60)
        if end_min < 10:
            print(f"{abs(end_time_m)}:0{end_min} hours before the start")
        else:
            print(f"{abs(end_time_m)}:{end_min} hours before the start")
        quit()
    end_time_m = abs(end_time)
    print(f"{abs(end_time_m)} minutes before the start")
if on_time != 0:
    if end_time >= 60:
        end_time_m = end_time // 60
        end_min = end_time - (end_time_m * 60)
        if end_min < 10:
            print(f"{abs(end_time_m)}:0{end_min} hours after the start")
        else:
            print(f"{abs(end_time_m)}:{end_min} hours after the start")
        quit()
    if end_time == 0:
        quit()
    end_time_m = abs(end_time)
    print(f"{abs(end_time_m)} minutes before the start")
