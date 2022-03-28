#输入一段英文，统计重复单词
string = input()
list_1 = []
dict_1 = {}
list_1 = string.split(' ')
for i in list_1:
    if i in dict_1:
        dict_1[i] += 1
    else:
        dict_1[i] = 1
for key,value in dict_1.items():
    print('%s \t %d' %(key,value))
