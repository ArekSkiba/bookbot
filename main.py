def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_count = get_char_count(text)
    report_list = convert_dict_to_list(character_count)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"({word_count} words found in the document) \n")
    print(*report_list, sep ='\n')
    print("--- End report ---")

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

def convert_dict_to_list(dictionary):
    dict_list = []
    for x, y in dictionary.items():
        dict_convert = {}
        if x.isalpha():
            dict_convert = {"char": x, "count": y}
            dict_list.append(dict_convert)
    dict_list.sort(reverse=True, key=sort_on)

    report_list = []
    for x in dict_list:
        char = list(x.values())[0]
        count = list(x.values())[1]
        report_list.append(f"The '{char}' character was found {count} times")
    return report_list    

def sort_on(dict):
    return dict["count"]

main()

