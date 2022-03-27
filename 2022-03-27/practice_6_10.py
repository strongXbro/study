favorite_number = {
    'David' : [2,5,7],
    'Mike' : [1,3,6],
    'Kangkang' : [3,9],
    'John' : [8,3,7],
    }
for name,numbers in favorite_number.items():
    print('%s\' favorite numbers are:' %name)
    for number in numbers:
        print(number)
