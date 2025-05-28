import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# 1. Load the dataset
df = pd.read_csv("large_spam_email_dataset.csv")  # Ensure this file is in your working directory

# 2. Extract features and labels
emails = df['email']
labels = df['label']

# 3. Convert text to numerical features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails)

# 4. Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.3, random_state=42)

# 5. Train Naive Bayes classifier
model = MultinomialNB()
model.fit(X_train, y_train)

# 6. Evaluate accuracy
y_pred = model.predict(X_test)
# print(" y_pred", y_pred)
print(" y_pred", len(y_pred))
# print(" y_test", y_test)
print(" y_test", len(y_test))
print("Accuracy:", accuracy_score(y_test, y_pred))

# 7. Test with a new email
new_email = ["Congratulations! You have won a free iPhone"]
new_data = vectorizer.transform(new_email)
prediction = model.predict(new_data)
print("Prediction:", "Spam" if prediction[0] == 1 else "Not Spam")
