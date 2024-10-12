name = input('Enter a username ')
x = len(name)
y = name.count(' ')
v = name.isdigit()
if x >= 12:

    print('please write less than 12 characters')
elif y >= 1 :
    print('NO SPACES')
elif v :
    print('no digits please')
else:
    print(f'welcome to the club {name}!')


