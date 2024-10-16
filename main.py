def main():
    book_path = "books/frankenstein.txt"
    print_report(book_path)

def get_book_text(book_path):
    with open(book_path) as file:
        return file.read()

def get_number_of_words(book_text):
    return len(book_text.split())

def get_character_counts(book_text):
    character_counts = {}
    for character in book_text.lower():
        if character in character_counts:
            character_counts[character] += 1
        else:
            character_counts[character] = 1
    return character_counts

def character_dict_to_sorted_list(character_dict):
    sorted_list = []
    for character, count in character_dict.items():
        sorted_list.append((character, count))
    sorted_list.sort(key=lambda x: x[1], reverse=True)
    return sorted_list

def print_report(book_path):
    book_text = get_book_text(book_path)
    number_of_words = get_number_of_words(book_text)
    character_counts = get_character_counts(book_text)
    character_sorted_list = character_dict_to_sorted_list(character_counts)
    print(f"--- Begin report of {book_path} ---")
    print(f"{number_of_words} words are found in the document")
    print("\n")
    for item in character_sorted_list:
        if item[0].isalpha():
          print(f"The '{item[0]}' character was found {item[1]} times")  
    print("--- End report ---")

main()