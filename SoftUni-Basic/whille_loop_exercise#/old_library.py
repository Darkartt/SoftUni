book_we_search = input()

book_count = 0

is_book_found = False


while True:

    current_book = input()

    if book_we_search == current_book:
        is_book_found = True
        print(f'You checked {book_count} books and found it.')
        break
    if current_book == 'No More Books':
        break
    book_count += 1



if not is_book_found:
    print(f'The book you search is not here!')
    print(f'You checked {book_count} books')