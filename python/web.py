print('welcome to this secret web. To enter, enter the password ')
password = input('Enter password: ')

if password == 'PASSWORD':      
    print('access granted')
    tit = input('hi,and wecome to this website maker, enter the title for the website : ') 
    sub = input('enter now your subheading ')
    mt = input ('now enter the main text ')
    print('proccesing...')
    print('...')
    print('congrats! your auto web')


    print(f'                  {tit}                                     ')
    print(f'                  {sub}                                     ')
    print(f'{mt}')
else:
    print('access denied')
