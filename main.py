import sys
from stats import get_num_words
from stats import count_char
from stats import report

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
# Opens the file in the desired path, and saves it's content into the 'f' variable
# and then returns it's values as string
def get_book_text(file_path):
    with open(file_path, encoding="utf-8") as f:
        return f.read()

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    #get_book_text("books/frankenstein.txt")
    num_words = get_num_words(get_book_text(sys.argv[1]))
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    #num_chars = count_char(get_book_text("books/frankenstein.txt"))
    #print(num_chars)
    sorting = report(count_char(get_book_text(sys.argv[1])))
    for item in sorting:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main()