import random
import string
store = {}
def shorten(url):
  code=''.join(random.choice(string.ascii_letters+string.digits)for _ in range(6))
  store[code] = url
  return code
def redirect(code):
 return store.get(code,"code not found")
print("1.shorten url")
print("2.redirect using code")
choice = input("enter your choice:")
if choice == "1":
  url = input("enter the url:")
  short_code = shorten(url)
  print("shorten code:",short_code)
elif choice == "2":
  code = input("enter the short code: ")
  print("original url:",redirect(code))
else:
  print("invalid choice")
