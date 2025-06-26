from stats import word_count, book_count, sort_count
import sys 

def get_book_text(filepath):
    with open(filepath,'r' ) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath= sys.argv[1]
    text =get_book_text(filepath)
    book_text = book_count(text)
    sorted_counts = sort_count(book_text)
    
    
   
    for i in sorted_counts:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['num']}")
    
if __name__ == "__main__":
    main()

    