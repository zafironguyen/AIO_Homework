string_1 = 'Happiness'


def letter_count(string):
    dict = {}
    for letter in string:
        count = dict.get(letter,0)
        dict[letter] = count+1
    return dict

print(letter_count(string_1))
