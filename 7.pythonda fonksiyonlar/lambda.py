def square(num): return num**2

result = square(2)
print(result)


# elimizde liste varsa
def square(num): return num**2

numbers =[1,3,5,9]

result= list(map(square,numbers))

print(result)

for item in map(square,numbers):
    print(item)



#LAMBDDA

nummbers = [1,3,5,9]

result=list(map(lambda num: num**2,numbers))

print (result)

# veya

square = lambda num: num ** 2

numbers = [1,3,5,9]

result=list(map(square,numbers))
print(result)

#karesini aldıklarımızın sadece çift olanları döndürme örneği

numbers = [1,3,5,9,10,4]

def check_even(num): return num%2==0
result = list(filter(check_even,numbers))
#result=list(filter(lambad num:num%2==0, nubers))


# veya 
#check_even = lambda num:num%2==0
#result list(filter(check_even,numbers))

#result = check_even(numbers[2])

print(result)