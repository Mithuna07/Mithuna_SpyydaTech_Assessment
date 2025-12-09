line = input().lower()
line = line.replace(",","").replace(".","")
words = line.split()
freq = {}
for word in words:
  if word in freq:
    freq[word] += 1
  else:
    freq[word] = 1

sorted_words = sorted(freq.items(), key=lambda x:x[1], reverse=True)
for word, count in sorted_words:
  print(word, "-" , count)
