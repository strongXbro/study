cities = {
    'chongqing' : {
        'country' : 'china',
        'population' : '30 million',
        'fact' : '山城,雾都,世界上桥梁最多的城市',
        },
    'chengdu' : {
        'country' : 'china',
        'population' : '21 million',
        'fact' : '拥有熊猫基地',
        },
    'beijing' : {
        'country' : 'china',
        'population' : '22 million',
        'fact' : '中国首都',
        },
    }
for city,contents in cities.items():
    print('%s '%city)
    for key,content in contents.items():
        print('%s : %s'%(key,content))
