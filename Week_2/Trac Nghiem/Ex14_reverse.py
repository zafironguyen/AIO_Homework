def reverse(x):
    return x[::-1]


if __name__ == "__main__":
    x = 'I can do it'
    assert reverse(x) == "ti od nac I"

    x = 'apricot'
    print(reverse(x))