import translator

def unit_test():
    test_case = [
        "Hello, My name is TackHyun Jung",  # correct input
        "i love black pink",  # correct input
        "have a nice day",  # correct input
        "'Hello",  # test for the translation of the world 'Hello
        "",  # test for null input
        "123456"]  # number input

    for case in test_case:
        german_text = translator.Translation().englishtogerman(case)
        print(german_text)

if __name__ == '__main__':
    unit_test()

