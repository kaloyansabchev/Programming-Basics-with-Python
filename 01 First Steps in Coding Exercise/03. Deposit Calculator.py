deposit_sum = float(input())
deposit_term = int(input())
interest_for_year = float(input())

total_sum = deposit_sum + deposit_term * ((deposit_sum * interest_for_year * 0.01) / 12)
print(total_sum)