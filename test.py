# ask the user for the multiplicator
# ask what is the maximum number the program should get to
# ask initial/starting number
# the program will multiply the initial number by multiplicator and will keep multiplicating
# until it reached the maximmum number
# each time, it will show 1 - the current result, 2 - the current step, 
# 3 - current time, 4 - time difference between last step and this one (to understand the performance)
# when the program reach the maximum number it will show: 1 - number of steps taken
# 2 - avergae time for each step, 3 - minimum time for steo, 4 - maximum time for step

stn = int(input('enter a starting number '))
mul = int(input('enter a multiplicator '))
en =  int(input('enter a maximum number '))
res = stn

while stn >= en:
    print(' you entered a maximum number inferior to the starting number')
    stn = int(input('enter a starting number '))
    en =  int(input('enter a maximum number '))
#we need to make sure that the last result is not greater than max result.
while res < en:
    res = res*mul
    print(res)
