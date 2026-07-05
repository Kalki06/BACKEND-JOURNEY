# Create a set of five fruits and print each fruit.
fruits= set()
fruits= {"mango", "banana", "apple", "kiwi", "grapes"}

for fruit in fruits:
    print(fruit)

# Ask the user for a fruit and check if it exists in the set.

user = input("Enter the fruit name ot check : ")
print(user in fruits)

'''
Create two sets and print:
Union
fruit2 = set()
fruit2 = {"pineapple", "watermenlon", "melon"}

print(fruits.union(fruit2))

Intersection
Difference
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}

print(whole_numbers.intersection(even_numbers))
print(even_numbers.issubset(whole_numbers))
'''

list = {1, 2, 4, 5 ,5 , 6,3, 2 ,1, 7}

set(list)
print(list)