import random
# user enter the number that like
my_number = input('What is your number: ')
my_number = int(my_number)
# user defind a range for guess his number
lower_range = input('What is your lower range? ')
upper_range = input('What is your upper range? ')
lower_range = int(lower_range)
upper_range = int(upper_range)

# this function randomly select a number in range that user defined it


def rand(lower_range, upper_range):
    guess = random.randint(lower_range, upper_range)
    return guess


# call the function
guess = rand(lower_range, upper_range)
# a loop for check condition and return amount base on the guess number
while guess != my_number:
    if guess < my_number:
        lower_range = guess
        upper_range = upper_range
        print('lower_range = ', lower_range)

    else:
        upper_range = guess
        lower_range = lower_range
        print('upper_range = ', upper_range)
# call function for continue process
    guess = rand(lower_range, upper_range)
# finish the loop and find the answer
print('The correct answer is equal to', guess)
