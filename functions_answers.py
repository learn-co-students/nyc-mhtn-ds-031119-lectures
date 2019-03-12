# Make a function to determine if a number is odd or even

def odd_even(number):
    # Check if the number is even with modulus
    if number % 2 == 0:
        # Set the return value equal to the string Even
        num = 'Even'
    else:
        # The other case is Odd, so use the else statement to get all the odd numbers
        num = 'Odd'
    return num

# Make a function that takes in a list of numbers and returns the numbers that are even

def even_list(numbers):
    # Make an empty list for the even numbers
    even_list = []
    # check if a number is even
    for number in numbers:
        if number % 2 == 0:
            even_list.append(number)
    # using list comprehension
    even_list_com = [x for x in numbers if x % 2 == 0]
    return  even_list # even_list_com # works as well

# Diven a list return the unique names in the list

def unique_names(list_of_names):
    # Use the set function in python
    return list(set(list_of_names))

# Make a function that determines if a word is a palandrome
# Should return true or false

def palindrome_detector(string):
    # using the index to reverse the string
    return string == string[::-1]





print(odd_even(4))
print(odd_even(139))
print(even_list([1,3,4,6,7]))
print(unique_names(['john', 'john', 'john']))
print(palindrome_detector('racecar'))
print(palindrome_detector('not'))
