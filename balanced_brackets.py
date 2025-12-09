s= input().strip()
stsck - []
for ch in s:
  if ch == '(' or ch == '{' or ch == '[':
    stack.append(ch)
  elif ch == ')' or ch =='}' or ch == ']':
    if not stack:
      print("false")
      exit()
    top = stack.pop()
    if (ch == ')' and top != '(') or \
       (ch == '}' and top != '{') or \
       (ch == ']' and top != '['):
         print("false")
         exit()
if not stack:
  print("true")
else:
  print("false")
    
