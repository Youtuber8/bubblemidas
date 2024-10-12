# first we define the the functions and it's parameters
def answer(name,number) :
    # we create a new variable
    maximum = 100
    # we calculate the variable maximum whith the info stored in variable number 
    if  number  >=  maximum :
        print('error error system crashing')
    else:
        for counter in range(number) :
            print(name)











# the program asks the question that what is your name in english and answer stored in variable
name = input('what is your name in english? ')
number =   int(input('how many times this name shoud be written? '))
answer(name,number)