def main():
        
        book_text = get_book_text("books/frankenstein.txt")
        count = count_words(book_text)
        chars = char_count(book_text)
        print_book_report(book_text, count, chars)
        

def count_words(book_content):
    words = book_content.split()
    count = len(words)
    return count

def get_book_text(path) :
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def char_count(book_content):
    chars_count = {}
    for char in book_content:
        chars_count[char.lower()] = chars_count.get(char.lower(), 0) + 1
    return chars_count

def print_book_report(book_content, word_count, chars):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document \n")
    
    for char in chars:
        if char.isalpha():
            count = chars.get(char, 0)
            print(f"The '{char}' character was found {count} times")
    
    print("\n--- End report ---")

main()