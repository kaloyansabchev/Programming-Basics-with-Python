total_pages = int(input())
pages_per_hour = int(input())
days = int(input())

total_time = total_pages / pages_per_hour
result = total_time / days
print(result)