# Print numbers from 1 to 20.
# for i in range(1, 21):
#     print(f"{i}\n ")


# Print all even numbers from 1 to 50.
# n = 50
# # for i in range(0, n+1, 2):
# #     print(f"{i}\n ")

# for i in range(0, n+1):
#     if(i%2 == 0):
#         print(f"{i}\n ")


# Find the sum of numbers from 1 to 100.
# n = 100
# total = 0
# for x in range(n+1):
#     total = total + x

# print(total)
    

# Print the multiplication table of any number entered by the user.
n = int(input("Enter the number to print multiplication table : "))

for i in range(1, 11):
    prod = n*i
    print(f"{n} * {i} = {prod}")