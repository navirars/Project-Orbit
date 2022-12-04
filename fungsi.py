import re
import pandas as pd
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords


# Fungsi untuk Membersihkan Text

def casefolding(text):
  text = text.lower()                               # Mengubah teks menjadi lower case
  text = re.sub(r'https?://\S+|www\.\S+', '', text) # Menghapus URL
  text = re.sub(r'[-+]?[0-9]+', '', text)           # Menghapus angka
  text = re.sub(r'[^\w\s]','', text)                # Menghapus karakter tanda baca
  text = re.sub(r"(.)\1{2,}",r"\1", text)           # Menghapus duplikasi data
  text = re.sub(r'^RT[\s]+', '', text)
  text = text.strip()
  return text
  
# Fungsi untuk Menghapus Stopwords

more_stopwords = pd.read_csv("english stopwords.csv")
more_stopwords.columns = ['stopwords'] # Tambahkan kata dalam daftar stopword

def remove_stop_words(text,stop_word):
  filtered_sentence = []
  word_tokens = word_tokenize(text) 
  filtered_sentence = [w for w in word_tokens if not w in stop_word] 
  return " ".join(filtered_sentence)

# Fungsi untuk Melakukan Stemming
def stemming(text,porter):
    token_words=word_tokenize(text)
    token_words
    stem_sentence=[]
    for word in token_words:
        stem_sentence.append(porter.stem(word))
        stem_sentence.append(" ")
    return "".join(stem_sentence)

# Fungsi untuk Text Pre-Processing
def text_preprocessing_process(text,stop_word,porter):
  text = casefolding(text)
  text = remove_stop_words(text,stop_word)
  text = stemming(text,porter)
  return text