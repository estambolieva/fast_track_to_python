'''
this file prepares dirty data for solving the problem of median maintenance
# median maintenance expected input:
  A stream of numbers
  - positive
  - negative
  -0
# median maintenance dirty input:
  A stream of objects
  - positive numbers
  - negative numbers
  - 0
  - strings
  - null
  - dates
  - 1,234
  - objects
'''

from random import uniform, randint
from random import choice
from string import lowercase
from datetime import datetime

def generate_dirty_data(length):
    data = []
    count = 0
    # while we have not generated more entries than desired
    while length > 0:
        # decide on what to generate
        gen_keys = ['num','str','null','date','funny_num', 'obj']
        # allow only 20% noise in the data
        allowed_noise_percecntage = 0.2
        # decide on wht to generate
        percentage = count/float(length)
        rand_ind = 0
        if percentage < allowed_noise_percecntage:
            rand_ind = randint(0, len(gen_keys)-1)
        if rand_ind == 0:
            rand_num = uniform(-100000, 100000)
            data.append(rand_num)
        if rand_ind == 1:
            rand_word = randomword()
            data.append(rand_word)
            count += 1
        if rand_ind == 2:
            data.append(None)
            count += 1
        if rand_ind == 3:
            # get current time
            now = datetime.now()
            data.append(now)
            count += 1
        if rand_ind == 4:
            # generate funny numbers like 1,23 instead of 1.23
            funny_num = ""
            first = randint(1,9)
            funny_num += str(first)
            funny_num += ","
            rand_decimal_count = randint(1,4)
            for i in range(rand_decimal_count):
                decimal = randint(0,9)
                funny_num += str(decimal)
            data.append(funny_num)
            count += 1
        if rand_ind == 5:
            # add objects to the data
            employee = MarioneteEmployee(randomword(), randint(18,60))
            data.append(employee)
            count += 1
        length -= 1
    return data


class MarioneteEmployee(object):
    name = ""
    age = 0

    # The class "constructor" - It's actually an initializer
    def __init__(self, name, age):
        self.name = name
        self.age = age


def randomword():
    return ''.join(choice(lowercase) for i in range(10))


if __name__ == "__main__":
    # number of randomly generated data entries
    length = 100
    data = generate_dirty_data(length)
    # store data into a file - 1 entry == 1 line
    with open("data.txt", "w+") as f:
        for datum in data:
            f.write("%s\n" % str(datum))

