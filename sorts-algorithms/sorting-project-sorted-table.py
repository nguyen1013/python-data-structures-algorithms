import utils
import sorts
from random import randrange, shuffle

bookshelf = utils.load_books('books_small.csv')
# bookshelf_v1 = bookshelf.copy()
# bookshelf_v2 = bookshelf.copy()
long_bookshelf = utils.load_books('books_large.csv')
long_bookshelf2 = long_bookshelf.copy()

for book in bookshelf:
  book['author_lower'] = book['author'].lower()
  book['title_lower'] = book['title'].lower()

def bubble_sort(arr, comparison_function):
  for i in range(len(arr)):
    for j in range(len(arr)-i-1):
      if comparison_function(arr[j],arr[j+1]):
        arr[j],arr[j+1] = arr[j+1],arr[j]
  return arr

def comparison_function(a,b):
  return a[0] > b[0]

def by_title_ascending(book_a, book_b):
  return comparison_function(book_a["title_lower"], book_b["title_lower"])

def by_author_ascending(book_a, book_b):
  return comparison_function(book_a["author_lower"], book_b["author_lower"])

def quicksort(list, start, end, comparison):
  if start>=end:
    return
  pivot_idx = randrange(start, end + 1)
  pivot_el = list[pivot_idx]

  list[end], list[pivot_idx] = list[pivot_idx], list[end]
  less_than_pointer = start

  for i in range(start, end):
    if comparison(pivot_el, list[i]):
      list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
      less_than_pointer +=1
  list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
  quicksort(list, start, less_than_pointer -1, comparison)
  quicksort(list, less_than_pointer+1, end, comparison)

def by_total_length(book_a, book_b):
  return len(book_a["author"]) + len(book_a["title"]) > len(book_b["author"]) + len(book_b["title"])


# sort_1 = bubble_sort(bookshelf, by_title_ascending)
# for book in sort_1:
#   print(book['title'])

# sort_2 = bubble_sort(bookshelf_v1, by_author_ascending)
# for book in sort_2:
#   print(book['author'])

# for book in bookshelf_v2:
#   print(book['author'])
# print("\n")

# quicksort(bookshelf_v2, 0, len(bookshelf_v2)-1, by_author_ascending)
# for book in bookshelf_v2:
#   print(book['author_lower'])

quicksort(long_bookshelf, 0, len(long_bookshelf)-1, by_total_length)
for book in long_bookshelf:
  print(book)

print("\n")
print("\n")

# sort_3 = bubble_sort(long_bookshelf2, by_total_length)
# for book in long_bookshelf2:
#   print(book)




















