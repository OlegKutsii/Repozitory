from random import randint

result_array = set()
def get_numbers_ticket (min_value, max_value, quantity):
    try:
        while len(result_array) != quantity:
            result_array.add(randint(min_value, max_value))
            if max_value - min_value <= quantity:
               return list() 
        return sorted(list(result_array))
    except ValueError:
        return list ()
lottery_numbers = get_numbers_ticket(1, 100, 6)
print("Your lottery numbers:", lottery_numbers)