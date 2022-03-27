favorite_places = {
    'Mike' : ['稻城','三亚'],
    'Ahuan' : ['故宫','大理','布达拉宫'],
    'Divid' : ['草原','沙漠','青海湖'],
    }
for name,places in favorite_places.items():
    print('%s\' favorite place are '%name)
    for place in places:
        print(place)
