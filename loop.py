number = int(input('Please enter your number: '))
count = 0
num = 0
# This loop will continue till the input equal to -1 and it will give us the average of all number that takes from user
while num != -1:
    number += num
    count += 1
    print(number, count)
    num = int(input('Please enter your number: '))

avg = number/count
print(avg)
