from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()

texts = []
with open('data/SMSSpamCollection') as f:
    for line in f:
        texts.append(line.rstrip().split("\t"))

# Create bag of words
bag_words = count_vect.fit_transform([t[1] for t in texts])

# Show words and counts
count_vect.vocabulary_
