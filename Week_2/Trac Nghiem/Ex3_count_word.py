def count_word(file_path):
    counter = {}
    with open(file_path, 'r', encoding='UTF-8') as file:
        for line in file:
            words = line.lower().split()
            for word in words:
                count = counter.get(word, 0)
                counter[word] = count + 1
    return counter

path = 'D:\\AIO-homework\\Module 1\\Week_2\\Trac Nghiem\\P1_data.txt'

result = count_word(path)
assert result['who'] == 3
print(result['man'])