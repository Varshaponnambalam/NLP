from nltk.stem import PorterStemmer

text = "Cats are running and jumping"

words = text.split()

ps = PorterStemmer()

stemmed_words = []
for word in words:
    stemmed_words.append(ps.stem(word))

print("Original text:", text)
print("Tokenized words:", words)
print("Stemmed words:", stemmed_words)