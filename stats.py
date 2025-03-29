import string


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_num_word(book_text):
    word_list = book_text.split()
    return len(word_list)

def count_char(book_text):
    word_dict = {}
    book_text = book_text.lower()

    for char in book_text:
        if char in string.ascii_lowercase:  # Only count a-z characters
            if char in word_dict:
                word_dict[char] += 1
            else:
                word_dict[char] = 1
    return word_dict

def sort_char_counts(char_dict):
    # Convert the dictionary into a list of dictionaries
    sorted_list = [{'character': char, 'count': count} for char, count in char_dict.items()]

    # Sort the list by the 'count' key in descending order
    sorted_list.sort(key=lambda x: x['count'], reverse=True)

    return sorted_list