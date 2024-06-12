def character_count(word):
    character_statistic = {}
    for letter in word:
        count = character_statistic.get(letter, 0)
        character_statistic[letter] = count+1

    return character_statistic


<<<<<<< HEAD
if __name__ == "__main__":
    assert character_count("Baby") == {'B': 1, 'a': 1, 'b': 1, 'y': 1}
    print(character_count('smiles'))
=======
assert character_count("Baby") == {'B': 1, 'a': 1, 'b': 1, 'y': 1}
print(character_count('smiles'))
>>>>>>> 46b7aa2acfdc84d7b926c61c796cc963115e9b72
