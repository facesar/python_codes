# Python Program to Remove Odd or Even Numbers From a List
# Below is how we can define a Python function to remove all the odd numbers from a Python list:

x = [12, 15, 7, 9]

def remove_odd(x):
    for i in x[:]:
        if (i % 2) != 0:
            x.remove(i)
    return x

print (remove_odd(x))

""" Just like the function defined above, 
below is how we can define a Python function to remove all
the even numbers from a Python list:"""

y = [12, 15, 7, 9]

def remove_even(x):
    for i in x[:]:
        if (i % 2) == 0:
            x.remove(i)
    return x

print(remove_even(y))
