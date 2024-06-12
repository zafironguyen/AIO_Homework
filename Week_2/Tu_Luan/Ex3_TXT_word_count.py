def word_count_txt(link):
    word_dict = {}
    with open(link, 'r', encoding='UTF-8') as file:
        for line in file:
            words = line.split()
            for word in words:
                count = word_dict.get(word, 0)
                word_dict[word] = count + 1
    return word_dict


<<<<<<< HEAD:Week_2/Tu_Luan/Ex3_TXT_word_count.py
if __name__ == "__main__":
    path = 'D:\\AIO-homework\\Module 1\\Week_2\\P1_data.txt'
    print(word_count_txt(path))
=======
path = 'D:\\AIO-homework\\Module 1\\Week_2\\P1_data.txt'
print(word_count_txt(path))
>>>>>>> 46b7aa2acfdc84d7b926c61c796cc963115e9b72:Week_2/Tu_Luan/Ex_3-TXT_word_count.py
