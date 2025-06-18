# Bookshelf 0                   Bookshelf 1
# Bookshelf 2                   Bookshelf 3
# Bookshelf 4                   --Bookshelf 5-- (periodicals)
# Bookshelf 6                   Bookshelf 7
# Bookshelf 8                   Bookshelf 9
# --Bookshelf 10-- (new books)  --Bookshelf 11-- (new books)

import math
import sys

books = []
with open("/home/nox/organization/library.org", "r", encoding="utf-8") as f:
    lines = f.readlines()
    book_lines = list(filter(lambda x: x.startswith("+"), lines))
    for book_line in book_lines:
        books.append(book_line.lstrip("+ ").strip())

number_of_bookshelves = 11
number_of_unused_bookshelves = 3
number_of_valid_bookshelves = number_of_bookshelves - number_of_unused_bookshelves
number_of_books = len(books)
books_per_bookshelf = math.ceil(number_of_books / number_of_valid_bookshelves)

bookshelves = []
for i in range(0, len(books), books_per_bookshelf):
    bookshelves.append(books[i:i + books_per_bookshelf])

current_bookshelf = 0
for bookshelf in bookshelves:
    print(current_bookshelf)
    current_bookshelf += 1

    for book in bookshelf:
        print("\t" + book)
