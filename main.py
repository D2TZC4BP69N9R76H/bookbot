import sys
from stats import (
    get_num_words, 
    count_chars, 
    chars_dict_to_sorted_list
)

def get_book_text(path_to_file: str) -> str:
    file_contents = ""

    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def print_report(book_path: str, num_words: int, chars_sorted_list: list[dict[str, int]]):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

def main():
    # book_path = "books/frankenstein.txt"

    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = count_chars(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print_report(book_path, num_words, chars_sorted_list)

main()