import sys
from stats import get_word_count, get_char_dict, transform_char_dict

def get_book_text(file_path: str):
    with open(file_path) as file:
        contents = file.read()
        return contents
    
def print_report(file_path, word_count, char_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    for dict_char in char_list:
        if dict_char["char"].isalpha():
            print(f"{dict_char["char"]}: {dict_char["num"]}")

    print("============= END ===============")
    
def main():
    arguments = sys.argv
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    
    book_text = get_book_text(sys.argv[1])
    word_count = get_word_count(book_text)
    char_dict = get_char_dict(book_text)
    char_list = transform_char_dict(char_dict)

    print_report(sys.argv[1], word_count, char_list)

main()