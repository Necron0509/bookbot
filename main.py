from stats import get_num_word, get_book_text, count_char, sort_char_counts
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = sys.argv[1]


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")

    # Read the book text
    book_text = get_book_text(book)

    # Word count
    num_words = get_num_word(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    # Character count
    all_char_counts = count_char(book_text)
    sorted_char_counts = sort_char_counts(all_char_counts)

    print("--------- Character Count -------")
    for char_data in sorted_char_counts:
        char = char_data['character']
        count = char_data['count']
        print(f"{char}: {count}")

    print("============= END ===============")



if __name__ == "__main__":
    main()