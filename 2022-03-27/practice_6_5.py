rivers = {
    'yangtae' : 'china',
    'Yellow River' : 'china',
    'Brahmaputra' : 'china'
        }
for nile,egypt in rivers.items():
    print('The %s runs through %s' %(nile.title(),egypt.title()))
print('---------求键----------')
for nile in rivers.keys():      #for nile in rivers:
    print(nile)
print('---------求值-----------')
for egypt in set(rivers.values()):   #set() 集合,集合中的每个元素都是独一无二的
    print(egypt)
