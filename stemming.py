from nltk.stem import PorterStemmer

text = "Cats are running"

words = text.split()

stemmer = PorterStemmer()

stemmed_words = []
for word in words:
    stemmed_words.append(stemmer.stem(word))
print("Original text:", text)
print("Tokenized words:", words)
print("Stemmed words:", stemmed_words)