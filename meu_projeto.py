import pandas as pd
from sklearn.model_selection import train_test_split

# Correção no caminho do arquivo e nome dos parâmetros
df = pd.read_csv('amazon_cells_labelled.txt', names=['review', 'sentiment'], sep='\t')


reviews = df['review'].values
sentiments = df['sentiment'].values

# Correção no train_test_split
reviews_train, reviews_test, sentiment_train, sentiment_test = train_test_split(
    reviews, sentiments, test_size=0.2, random_state=500
)

print(reviews_train, reviews_test, sentiment_train, sentiment_test)

