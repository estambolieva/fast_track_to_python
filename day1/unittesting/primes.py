def is_prime(number):
    """ Returns true if number is prime """
    for element in range(2, number):
        if number % element == 0:
            return False

    # else
    return True

def print_next_prime(number):
    """ Prints the closes prime number bigger than 'number' """
    index = number
    while True:
        index += 1
        if is_prime(index):
            print index