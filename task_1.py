def convert_to_uah(amount, rate=41.5):
    sum = amount * rate
    return sum

first_case_amount = 100
first_case = convert_to_uah(first_case_amount)

second_case_amount = 100
second_case_rate = 38.0
second_case = convert_to_uah(second_case_amount, second_case_rate)

print("$100:")
print(f"Курс 41.5 UAH: {first_case} UAH")
print(f"Курс 38.0 UAH: {second_case} UAH")
