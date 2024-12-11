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
    count_dict = {}
    for x in text:
        lowered = x.lower()
        if lowered in count_dict:
            count_dict[lowered] += 1
        else:
            count_dict[lowered] = 1
    return count_dict

main()

