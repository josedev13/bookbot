def main():
    book_path = "frankenstein.txt"
    text = get_book_text(book_path)
    count = word_count(text)
    new_dict = string_count(text)
    new_sorted_list = char_dict_to_sorted_list(new_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{count} words found in the document")
    print()

    for item in new_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def word_count(path):
    counter = 0
    words = path.split()
    for word in words:
        counter += 1
    return counter

def string_count(path):
    counts = {}
    text_lower = path.lower()
    for char in text_lower:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def sort_on(dict):
    return dict["num"]

def char_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for char in num_chars_dict:
        sorted_list.append({"char": char, "num": num_chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list



main()