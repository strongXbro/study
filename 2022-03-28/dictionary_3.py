list_1 = []
dict_1 = {}
i = 6102009001
while i <= 6102009100:
    list_1.append(i)
    i += 1
#print(list_1)

for n in list_1:
    if n not in dict_1:
        dict_1[n] = 'redhat'
for key,value in dict_1.items():
    print('%d \t %s' %(key,value))

