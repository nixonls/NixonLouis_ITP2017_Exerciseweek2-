import random
import time
z = []
t = []
total = []
store = 'OPEN'

service_tax = 21

t=0

print('Welcome to Burger Rasa!')
star = time.time()
list_of_item = {
    "Bun":[10, 5000],
    "Cheese":[10, 3000],
    "Meat":[10,4000],
    "Egg":[10, 3000],
    "Lettuce": [10, 2000]
}

print('Type of Burger, Random & Custom')
def item_system(a):
    x = 0
    list_of_item[a].insert(0,list_of_item[a][0]-1)
    list_of_item[a].pop(1)
    t.append(list_of_item[a][1])
    z.append(a)

def ran():
    y = random.randint(1,10)
    a = 0
    item_system('Bun')
    while y != 0:
        m = random.randint(1,4)
        if m == 1:
            item_system('Meat')
        elif m == 2:
            item_system('Cheese')
        elif m == 3 :
            item_system('Egg')
        elif m == 4 :
            item_system('Lettuce')
        y -=1
    for i in range (len(t)):
        a = 0
        a = a + t[i]
    a = a*(100+service_tax)/100
    total.append(a)
    print('Rp. ', a, z)

def user_input():
    print('The ingredients are')
    a = 0
    for i in list_of_item.keys():
        print(i, end = " ")
    while True:
        ing = input('Please input the ingredient! \n')
        item_system(ing,a)
        ing2 = input ('Do you wish to add more?')
        if ing2.upper == 'NO':
            break
    var = a * (100 + service_tax) / 100
    print('Rp. ',a,z)
    return t

while list_of_item['Bun'][0] != 0 or store == 'CLOSE':
    try :
        x = input('Please, input type of Burger ')
        if x.title() == 'Random':
            ran()
        elif x.title() == 'Custom':
            user_input()
        end = time.time()
        calc = int(end-start)
        if calc > 36000:
            store = 'START'
    except:
        print('Error, Try again')
