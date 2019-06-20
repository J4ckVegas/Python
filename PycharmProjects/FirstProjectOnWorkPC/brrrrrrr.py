str_r = 'pineapple'
str_i = 'penis'
res = "*" * len(str_r)

counter_i = 0
counter_j = 0

temp = list(res)

if str_r == str_i:
    print('win')
else:
    while counter_i < len(str_i):
        if str_i[counter_i] in str_r:
            while counter_j < len(str_r):
                if str_i[counter_i] == str_r[counter_j]:
                    temp[counter_j] = str_i[counter_i]
                counter_j += 1
            counter_j = 0
        counter_i += 1
    res = ''.join(temp)

    print(temp)
    print(res)
