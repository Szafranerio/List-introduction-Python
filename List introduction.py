bicycles  = ['electric', 'bmx', 'fixed', 'hybrid', 'cross', 'gravel'] #List is defined by []

print (bicycles)
#['electric', 'bmx', 'fixed', 'hybrid', 'cross', 'gravel']

print (bicycles[0]) #List is organized from 0. So the first will be electric [0], second will be bmx [1], etc.
#electric

print (bicycles[0].title()) #title() is capitalizing the first letter
#Electric

print (bicycles[-1].title()) #If user is using "-1" it will bring the last elemnt from the list
#Gravel

message = f"My first bike was {bicycles[1].title()}" #Adding the sentence to the list, bike is choosen by using [1], whihc is Bmx 
print(message) 
#My first bike was Bmx

cars = ['honda', 'bmw', 'merceds', 'kia', 'cupra', 'tesla']
cars[0] = 'volvo' #This command is chanigng the first value in the list from honda to volvo by using [0]
print(cars)
# ['volvo', 'bmw', 'merceds', 'kia', 'cupra', 'tesla']


cars = ['honda', 'bmw', 'merceds', 'kia', 'cupra', 'tesla'] 
cars.append('volvo') #.append is adding a value at the end of the list   
print(cars)
#['honda', 'bmw', 'merceds', 'kia', 'cupra', 'tesla', 'volvo']

cars = ['honda', 'bmw', 'merceds', 'kia', 'cupra', 'tesla'] 
cars.insert(0, 'volvo') #.insert is adding an element to the beggining of the list
print(cars)
#['volvo', 'honda', 'bmw', 'merceds', 'kia', 'cupra', 'tesla']

cars = ['honda', 'bmw', 'merceds', 'kia', 'cupra', 'tesla']
del cars [3] #del cars is removing an elemnt from the list. Remeber to use value in the []
print(cars)
#['honda', 'bmw', 'merceds', 'cupra', 'tesla']

cars = ['honda', 'bmw', 'merceds', 'kia', 'cupra', 'tesla']
popped_cars = cars.pop() #.pop() removes the last element from the list but that element is still is use an can be resotred
print(popped_cars)
#tesla

print(f'My last car was {popped_cars.title()}') #Even Tesla was not in the list it was still possible to work with it
#My last car was Tesla

cars = ['honda', 'bmw', 'merceds', 'kia', 'cupra', 'tesla']
cars.remove('honda') #.remove is deleting value from the list
print(cars)
#['bmw', 'merceds', 'kia', 'cupra', 'tesla']

brands = ['versace', 'zara', 'hm', 'gucci', 'supreme']
brands.sort() #.sort() sorts list in alphabetical order
print (brands)
#['gucci', 'hm', 'supreme', 'versace', 'zara']

brands = ['versace', 'zara', 'hm', 'gucci', 'supreme']
brands.sort(reverse=True) #.sort(reverse=True) orgnise list from Z to A
print(brands)
#['zara', 'versace', 'supreme', 'hm', 'gucci']

brands = ['versace', 'zara', 'hm', 'gucci', 'supreme']
len(brands) #len() is shwoing the number of values in the list. It can help to see the amount of users in the webpage or application

