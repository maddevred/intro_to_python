# comment
​
"""Welcome to Python"""
​
""" Data Types """
name = 'Rome'
age = 5
is_old = False
sei_1019 = True
​
name = 'Lev'
​
print(name)
​
""" Methods for a string """
sentence = 'Today is Nicole birthday'
​
nicole_birthday = sentence.split(' ')
print(nicole_birthday)
​
new_sentence = " ".join(nicole_birthday)
​
# find index
print(new_sentence.index('N'))
​
# Upper and Lower case
name.upper()
name.lower()
​
# replace
day_sentence = sentence.replace('birthday', 'Day')
print(day_sentence)
​
# in keyword
is_day = 'Day' in day_sentence
print(is_day)
​
day_sentence
​
# ranges
last_letter = day_sentence[-1]
nicole_range = day_sentence[9:15]
print(day_sentence[15])
print(nicole_range)
​
# length
print(len(nicole_range))
​
# logical operators
equal_to = 5 == 5
not_equal = 5 != 5
​
not True
not False
​
true_story = 5 <= 5
this_should_be_true = 6 >= 5
​
print(9 < 30)
​
print(5 < 4 or 6 > 30)
print('Rome' == 'rome' or 'Pete' == 'Pete')
print('Rome' == 'rome' and 'Pete' == 'pete')
​
print('' or 'Rome')
print(0 or 5)
​
print(5 < age < 6)
​
real_name = name or False