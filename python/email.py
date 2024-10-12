
email = input('enter your email so we can sell your personal photos and videos ')

index = email.index('@')

username = email[:index]
domain = email[index + 1:]

print(f'your username is {username} and domain {domain} ')
print(index)

