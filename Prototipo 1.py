import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

df = pd.read_csv('tutores.csv')
# Replace NaN with an empty string
df['Carrera '] = df['Carrera '].fillna('')
# Create a TfidfVectorizer and Remove stopwords
tfidf = TfidfVectorizer(stop_words='spanish, Carrera ')
# Fit and transform the data to a tfidf matrix
tfidf_matrix = tfidf.fit_transform(df['Carrera '])
# Print the shape of the tfidf_matrix
tfidf_matrix.shape