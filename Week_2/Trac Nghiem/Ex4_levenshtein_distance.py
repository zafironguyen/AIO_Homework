from ..Tu_Luan import Ex4_levenshtein_distance
levenshtein = Ex4_levenshtein_distance.levenshtein_distance

if __name__ == "__main__":
    assert levenshtein("hi", "hello") == 4
    print(levenshtein('hola', 'hello'))
