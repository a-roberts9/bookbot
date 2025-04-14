def number_of_words(text):
        new_list = text.split()
        return len(new_list)

def number_of_characters(book_text):
    all_lowercase = book_text.lower()
    char_counts = {}
    for character in all_lowercase:
            if character in char_counts:
                char_counts[character] += 1
            else:
                char_counts[character] = 1
    return char_counts

def sort_dict(char_counts):
    chars_list = []

    for char, count in char_counts.items():
        char_dict = {"char": char,"count": count}
        chars_list.append(char_dict)

    def sort_on(dict):
        return dict["count"]
   
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list
    