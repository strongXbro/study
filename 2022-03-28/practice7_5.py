a = True
while a:
    age = int(input('How old are you: '))
    if age < 3:
        print('Free tickets')
        a = False
    elif 3 <= age <= 12:
        print('ten Dollar')
        a = False
    else:
        print('fifteen Dollar')
        a = False
