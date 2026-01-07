import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import defaultdict

nltk.download('punkt')
nltk.download('stopwords')

def summarize_text(text, max_sentences=3):
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())

    stop_words = set(stopwords.words('english'))
    freq_table = defaultdict(int)

    for word in words:
        if word.isalnum() and word not in stop_words:
            freq_table[word] += 1

    sentence_scores = defaultdict(int)
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in freq_table:
                sentence_scores[sentence] += freq_table[word]

    summary = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
    return " ".join(summary[:max_sentences])
