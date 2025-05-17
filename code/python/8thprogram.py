# Install required packages if not already installed:
# pip install nltk scikit-learn pandas

import pandas as pd
import nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score

# Download stopwords if not already present
nltk.download('stopwords')
from nltk.corpus import stopwords
import string

# Sample Twitter dataset (replace with your own dataset for real application)
data = {
    'tweet': [
        "I love this phone!",
        "This movie is terrible...",
        "Had an awesome day today :)",
        "I hate waiting in traffic",
        "Such a boring game.",
        "Best concert ever!",
        "I'm so sad right now.",
        "What a great experience!",
        "Worst customer service.",
        "Feeling happy and blessed!"
    ],
    'sentiment': [
        'positive', 'negative', 'positive', 'negative', 'negative',
        'positive', 'negative', 'positive', 'negative', 'positive'
    ]
}

# Load the dataset into a pandas DataFrame
df = pd.DataFrame(data)

# Preprocessing function
def preprocess_text(text):
    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation])  # Remove punctuation
    tokens = text.split()  # Tokenize the text
    tokens = [word for word in tokens if word not in stopwords.words('english')]  # Remove stopwords
    return ' '.join(tokens)

# Apply preprocessing to each tweet
df['clean_tweet'] = df['tweet'].apply(preprocess_text)

# Convert text to feature vectors using CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['clean_tweet'])
y = df['sentiment']

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Naïve Bayes classifier
nb_classifier = MultinomialNB()
nb_classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = nb_classifier.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
