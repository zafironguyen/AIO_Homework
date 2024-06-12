def check_the_number(n):
    list_of_numbers = []
    for i in range(1, 5):
        # Your code here
        # Su dung append them i vao trong list_of_number
        list_of_numbers.append(i)
    if n in list_of_numbers:
        results = " True "
    else:
        results = " False "
    return results


if __name__ == "__main__":
    N = 7
    assert check_the_number(N) == " False "
    N = 2
    results = check_the_number(N)
    print(results)
