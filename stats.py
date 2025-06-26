def word_count(text):
    words = text.split()
    return len(words)

def book_count(string):
    string = string.lower()
    char_count = {}
    
    for char in string:
        if char in char_count:
            char_count[char]+= 1
        else:
            char_count[char] = 1
    return char_count
def sort_count(sort_dict):
    char_list = [{"char":char, "num":count} for char, count in sort_dict.items()]
    char_list.sort(reverse=True, key=lambda x:x["num"] )
    return char_list
