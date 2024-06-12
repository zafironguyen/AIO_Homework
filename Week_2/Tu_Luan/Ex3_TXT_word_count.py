def word_count_txt(link):
    word_dict = {}
    with open(link, 'r', encoding='UTF-8') as file:
        for line in file:
            words = line.split()
            for word in words:
                count = word_dict.get(word, 0)
                word_dict[word] = count + 1
    return word_dict


if __name__ == "__main__":
    path = 'D:\\AIO-homework\\Module 1\\Week_2\\P1_data.txt'
    print(word_count_txt(path))
