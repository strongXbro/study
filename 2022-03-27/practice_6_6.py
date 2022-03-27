favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
    }
take_the_survey = ['toy','jen','hello','world','phil','ahuan']
for name in take_the_survey:
    if name in favorite_languages:
        print('%s,Think you for your cooperation' %name)
    else:
        print('%s,Please take the survey' %name)

