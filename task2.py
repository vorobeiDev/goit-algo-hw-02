from collections import deque


def is_palindrome(string):
    string = ''.join(filter(str.isalpha, string)).lower()

    char_deque = deque(string)

    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False

    return True


def run():
    print(is_palindrome("Козак з казок."))
    print(is_palindrome("Козак з каaaaзок."))
    print(is_palindrome("Уже лисі ліси... Лежу."))
    print(is_palindrome("Уже ліси... Лежу."))
    print(is_palindrome("І що сало? Ласощі..."))
    print(is_palindrome("Я несу гусеня."))


if __name__ == '__main__':
    run()
