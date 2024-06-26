string_1 = 'Happiness'


def letter_count(string):
    result = {}
    for letter in string:
        count = result.get(letter, 0)
        result[letter] = count+1
    return result


if __name__ == "__main__":
    print(letter_count(string_1))
