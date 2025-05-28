from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 1. Sample dataset (text + labels)
emails = [
    "Win a lottery now",                  # spam
    "Limited time offer, claim prize",    # spam
    "You are selected for a free gift",   # spam
    "Important meeting at 10 AM",         # not spam
    "Project deadline is tomorrow",       # not spam
    "Let’s have lunch today",             # not spam
    "Earn money quickly from home",       # spam
    "Congratulations, you won a car",     # spam
    "Team meeting rescheduled",           # not spam
    "Monthly report attached",            # not spam
]

labels = [1, 1, 1, 0, 0, 0, 1, 1, 0, 0]  # 1 = spam, 0 = not spam

# 2. Convert text into numeric features
vectorizer = CountVectorizer()
"""
 creates an object called vectorizer that will convert text into numbers (specifically, a bag-of-words model).
 It takes all the unique words in your dataset and builds a vocabulary.
 Each word becomes a feature (like a column in a spreadsheet).
 🔤 Think of it as preparing a list of all words found in the emails.
"""

X = vectorizer.fit_transform(emails)
"""
fit → Learns all the words (vocabulary) from your email data.
transform → Converts each email into a numeric vector showing how many times each word appears.
The result X is a matrix of word counts:
Rows = individual emails
Columns = unique words
Values = how many times each word appears in that email
"""
# print(X)
# 3. Split into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.3, random_state=42)

print("X_train",X_train)
#print("X_test",X_test)
print("y_train",y_train)
#print("y_test",y_test)


# 4. Train Naïve Bayes classifier
model = MultinomialNB()
model.fit(X_train, y_train)

# 5. Predict on test data
y_pred = model.predict(X_test)

# 6. Evaluate
print("Predicted labels:", y_pred)
print("Actual labels:   ", y_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# 7. Try a new email
new_email = ["Congratulations! You have won a free iPhone"]
new_data = vectorizer.transform(new_email)
# print("new_Data", new_data)
prediction = model.predict(new_data)
print("Prediction for new email:", "Spam" if prediction[0] == 1 else "Not Spam")
