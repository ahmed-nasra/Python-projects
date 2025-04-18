library=[{'title':'The blue elephant', 'author':'ahmed mourad','year':2012}]
def add_book(ti, au, yr):
    book = {'title':ti, 'author':au, 'year':yr}
    library.append(book)
    print (f'{book} have been aded to your library')

def remove_book(ti):
    if not library:
        print('your library is empty')
    else:
        for book in library:
            if book['title'] == ti:
                library.remove(book)
                print(f'book {ti} have been removed')
                return
                
        print(f'book {ti} is not in not found')


def display_book():
    if not library:
        print('your library is empty')
    else:
        for book in library:
            print(f'title:{book['title']}, author:{book['author']} and year:{book['year']}')

def search_book(ti):
    if not library:
        print('your library is empty')
    else:
        for book in library:
            if book['title'] == ti:
                print(f'book {ti} is in your library')
                return
        print(f'book {ti} is not fount')
while True:
    print('\n *** Book_Manager ***')
    print('1. add_book')
    print('2. remove_book')
    print('3. display_book')
    print('4. search_book')
    print('5. exit')

    choice = int(input('Enter your choice'))

    if choice == 1:
        title = input('Enter your book name')
        author = input('Enter the book author')
        year = int(input('Enter book year'))
        add_book(title, author, year)

    elif choice == 2:
        title = input('Enter the book name you want to remove')
        remove_book(title)

    elif choice == 3:
        display_book()

    elif choice == 4:
        title = input('search by book name')
        search_book(title)

    elif choice == 5:
        print('exit')
        break

    else:
        print('invalid choice')
