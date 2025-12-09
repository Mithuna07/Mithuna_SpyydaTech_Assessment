library = []
def add_book():
  book_name = input("enter book name: ")
  library.append({"name":book_name, "borrowed":False})
def search_book():
  search_name = input("enter book name to search: ")
  found = False
  for book in library:
    if book["name"].lower() == search_name.lower():
      status = "borrowed" if book["borrowed"] else "available"
      print(f"book found: '{book['name']}' - {status}\n")
      found = True
      break
if not found:
   print("book not found.\n")
def borrow_book():
  borrow_name = input("enter book name to borrow: ")
  for book in library:
    if book["name"].lower() == borrow_name.lower():
      if not book["borrowed"]:
        book["borrowed"] = True
        print(f"you have borrowed '{book['name']}'.\n")
      else:
        print(f"'{book['name']}' is already borrowed.\n")
      return
 print("book not found.\n")
def return_book():
  return_name=input("enter book name to return: ")
  for book in library:
    if book["name"].lower() == return_name.lower():
      if book["borrowed"]:
        book["borrowed"] = False
        print(f"'{book['name']}' returned.\n")
      else:
        print(f"'{book['name']}' not borrowed.\n")
      return
print("book not found.\n")
def show_menu():
  print("library menu")
  print("1.add book")
  print("2.search book")
  print("3.borrow book")
  print("4.return book")
  print("5.exit")
while True:
  show_menu()
  choice = input("choose an option: ")
  if choice == "1":
    add_book()
  elif choice == "2":
    search_book()
  elif choice == "3":
    borrow_book()
  elif choice == "4":
    return_book()
  elif choice == "5":
    print("exit")
    break
  else:
    print("invalid input.\n")
    


