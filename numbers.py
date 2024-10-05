import random


def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity > max or quantity < min:
        print(
            "check parameters, 'min' and 'max' must be between 1 and 1000, "
            "'quantity' cannot exceed 'max' or be less than 'min'")
        return []
    else:
        numbers = random.choices(range(min, max), k=quantity)
        return sorted(numbers)


lottery_numbers = get_numbers_ticket(1, 49, 5)
print("Ваші лотерейні числа:", lottery_numbers)
