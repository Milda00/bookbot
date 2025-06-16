import sys
from curses.ascii import isalpha

from stats import count_words, count_characters, sort_dictionary


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = count_words(text)
    num_characters = count_characters(text)
    sorted_characters = sort_dictionary(num_characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at: {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("----------- Character Count ----------")
    for char in sorted_characters:
        if isalpha(char["char"]):
            print(f"{char["char"]}: {char["num"]}")

    print("============= END ===============")


main()
