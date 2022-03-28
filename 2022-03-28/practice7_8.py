sandwich_orders = ['Bacon','Fries','Egg cress','Lobster rolls','Poor Man']
finished_sandwiches = []
sandwich = ''
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)

for finished_sandwich in finished_sandwiches:
    print('I made your %s sandwich' %finished_sandwich)
