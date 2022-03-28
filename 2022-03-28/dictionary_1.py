#统计1000个随机数中重复的数字
'''
from random import randint
all_number = []
for number in range(1000):
    all_number.append(randint(20,100))
numbers = sorted(all_number)
dic = {}
for new_number in numbers:
    if new_number in dic:
        dic[new_number] += 1
    else:
        dic[new_number] = 1
for key,value in dic.items():
    print('%d\t%d'%(key,value))
'''
#'''
from random import randint
number = {}

for i in range(1000):
    new_number = randint(20,100)
    if new_number in number:
        number[new_number] += 1
    else:
        number[new_number] = 1
for key,value in number.items():
    print(key,value)
#'''
