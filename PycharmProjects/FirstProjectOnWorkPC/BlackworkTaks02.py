import random

array_of_elements = ["apple", "orange", "lemon", "banana", "apricot", "avocado", "broccoli",
                     "carrot", "cherry", "garlic", "grape", "melon", "leak", "kiwi", "mango",
                     "mushroom", "nut", "olive", "pea", "peanut", "pear", "pepper", "pineapple",
                     "pumpkin", "potato"]

hidden_element = random.choice(array_of_elements)
char_array = list(hidden_element)
print(hidden_element, ' - ', char_array)

open_element = random.choice(array_of_elements)
char_array2 = list(open_element)
print(open_element, ' - ', char_array2)

number_of_letters = len(hidden_element)
print('Кол-во букв в 1 слове: ', number_of_letters)
number_of_letters2 = len(open_element)
print('Кол-во букв в 2 слове: ', number_of_letters2)

letter_number1 = 0
letter_number2 = 0

while True:
    next_elem = hidden_element[letter_number1]
    letter_number1 += 1
    while True:
        next_elem2 = open_element[letter_number2]
        letter_number2 += 1

        if next_elem == next_elem2:
            print(next_elem, end='')

        if letter_number2 == number_of_letters2:
            letter_number2 = 0
            break

    #if next_elem != next_elem2:
     #   print('#', end='')

    if letter_number1 == number_of_letters:
        break
