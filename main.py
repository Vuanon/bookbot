def main():
    file_path = "books/frankenstein.txt"
    with open(file_path) as f:
        file_contents = f.read()
        print_report(file_contents, file_path)

def count_words(contents):
    return len(contents.split())

def count_char(contents):
    char_dict = {}
    for letter in contents.lower():
        if letter not in char_dict:
            char_dict[letter] = 1
        else:
            char_dict[letter] += 1
    return char_dict

def print_report(contents, file_path):
    word_count = count_words(contents)
    char_dict = count_char(contents)
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\n")
    alphabet_set = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}

    for alphabet in alphabet_set:
        print(f"The '{alphabet}' character was found {char_dict[alphabet]} times")
    
    print("--- End report ---")


    
    

main()
