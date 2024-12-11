def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_count = get_char_count(text)
    print(word_count, character_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    word_count = len(words)
    return word_count

def get_char_count(text):
    text_lower = text.lower()
    import string
    string.printable
    char_list = list(string.printable)

    count_dict = {}
    for x in char_list:
        char_count = text_lower.count(x)
        count_dict.update({x: char_count})
    return count_dict

main()

