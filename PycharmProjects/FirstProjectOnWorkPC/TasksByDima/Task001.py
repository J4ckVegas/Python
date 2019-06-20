import random


array_of_elements = ["apple", "orange", "lemon", "banana", "apricot", "avocado", "broccoli",
                     "carrot", "cherry", "garlic", "grape", "melon", "leak", "kiwi", "mango",
                     "mushroom", "nut", "olive", "pea", "peanut", "pear", "pepper", "pineapple",
                     "pumpkin", "potato"]

hidden_element = random.choice(array_of_elements)
char_array = list(hidden_element)
print(char_array)

"""
hidden_element2 = random.choice(array_of_elements)
hidden_element3 = random.choice(array_of_elements)
print('hd2: ', hidden_element2)
print('hd3: ', hidden_element3)
letter_number = 0
number_of_letters = len(hidden_element2)
print(number_of_letters)
while letter_number != number_of_letters:
    letter_number += 1
    one_letter = hidden_element2(letter_number)
    ol1 = hidden_element3.split(one_letter, '#')
    print(ol1)
"""

hidden_element2 = random.choice(array_of_elements)
hidden_element3 = random.choice(array_of_elements)
print('hd2: ', hidden_element2)
print('hd3: ', hidden_element3)
letter_number = 0
number_of_letters = len(hidden_element2)
print('Длинна hd2: ', number_of_letters)

while letter_number != number_of_letters:
    okey = hidden_element2[letter_number]
    letter_number += 1
    print('#', end='')
    for j in hidden_element3:
        if j == okey:
            print(j, end='')

