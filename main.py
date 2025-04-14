import sys

def main():
    from stats import number_of_words
    from stats import number_of_characters
    from stats import sort_dict
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]

    def get_book_text(file_path):
        with open(file_path) as f:
            file_contents = f.read()
            return file_contents
   
    
    book_text = get_book_text(file_path) 
    word_count = number_of_words(book_text)
    char_counts = number_of_characters(book_text)
    sorted_chars = sort_dict(char_counts)
   
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"{word_count} words found in the document")
    print("--------- Character Count -------") 

    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]

        if char.isalpha():
            print(f"{char}: {count}")
   
    print("============= END ===============")
main()