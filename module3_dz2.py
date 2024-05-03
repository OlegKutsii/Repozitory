from random import randint


def get_numbers_ticket (min_value, max_value, quantity):
    result_array = set()
    try:
        while len(result_array) != quantity:
            result_array.add(randint(min_value, max_value))
            if max_value - min_value < quantity:
               return list() 
        return sorted(list(result_array))
    except ValueError:
        return list ()
    
lottery_numbers = get_numbers_ticket(50, 100, 8)
   
if __name__ == '__main__':
    lottery_numbers = get_numbers_ticket(50, 100, 8)
    print("Your lottery numbers:", lottery_numbers)
    
    
    