name = input('what is your name ? ')
day = input ('when is your birthday? ')
date = input('what is the day today? ')


if day == date : 
    print(f'Happy birthday {name}!')
elif day == '':
    print('you have not introduced anything')

else : 
    print('Today is not your birthday')
