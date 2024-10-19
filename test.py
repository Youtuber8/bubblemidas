# ask the user for the multiplicator- d
# ask what is the maximum number the program should get to -d
# ask initial/starting number-d
# the program will multiply the initial number by multiplicator and will keep multiplicating
# until it reached the maximmum number-d
# each time, it will show 1 - the current result,-d 2 - the current step,-d
# 3 - current time, 4 - time difference between last step and this one (to understand the performance)
# when the program reach the maximum number it will show: 1 - number of steps taken
# 2 - avergae time for each step, 3 - minimum time for steo, 4 - maximum time for step



#pending work:  - time difference between last step and this one (to understand the performance)
# when the program reach the maximum number it will show: 1 - number of steps taken
# 2 - avergae time for each step, 3 - minimum time for steo, 4 - maximum time for step


from datetime import datetime
stn = int(input('enter a starting number '))
mul = int(input('enter a multiplicator '))
en =  int(input('enter a maximum number '))
res = stn
num = 0
allresults = []


while stn >= en:
    print(' you entered a maximum number inferior to the starting number')
    stn = int(input('enter a starting number '))
    en =  int(input('enter a maximum number '))

while res < en:
    res = res*mul
    num = num + 1
    now = datetime.now()
    if res > en :
        break
    else:
        results = [num , res , now ]
        allresults.append(results)
        
        print (f'step {num} result {res} current time {now}')
print(allresults)
         
        
            
        

