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

letter_counter = 0

res = "*" * len(hidden_element)
temp = list(res)

if hidden_element == open_element:
    print('win')
else:
    while letter_counter < min(len(open_element), len(hidden_element)):
        if open_element[letter_counter] == hidden_element[letter_counter]:
            temp[letter_counter] = open_element[letter_counter]
        letter_counter += 1
    res = ''.join(temp)

    print(temp)
    print(res)
