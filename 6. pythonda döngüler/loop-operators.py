
for item in range(10):
    print(item)
print(" ")  
for item in range(2,10):
    print(item)    

print(list(range(5,100,20)))  #liste şeklinde yazar


#enumerate
index = 0
greeting = 'Hello There'

for letter in greeting:
    print(f'index: {index} letter: {greeting[index]}')
    index+=1

for index, letter in enumerate(greeting):
    print(f'index: {index} letter: {letter}')

for item in enumerate(greeting):
    print(item)
    
#zip

list1= [1,2,3,4,5]
list2=['a','b','c','d','e']

print(list(zip(list1, list2)))

for item in zip(list1,list2):
    print(item)