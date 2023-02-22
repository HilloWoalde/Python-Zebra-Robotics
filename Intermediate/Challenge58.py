file = open("58Suggestions.txt")

text = file.read()

words = text.split()

file.close()

wordsToLookFor = {
  "password": 0,
  "security": 0,
  "e-transfer": 0,
  "accounts": 0,
  "cards": 0,
  "deposit": 0,
  "branch": 0,
}


for word in words:
    if word.lower().strip(',') in wordsToLookFor:
        wordsToLookFor[word.lower().strip(',')] += 1
for i in wordsToLookFor:
    print(i+" number of occurrences: "+str(wordsToLookFor[i]))
