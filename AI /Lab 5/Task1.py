import pandas as pd
import nltk
from nltk.corpus import stopwords
import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

# Step 1: Collect and Prepare Your Data
# Sample dataset
data = {
    'feedback': [
        "I love this product!",
        "This is the worst experience I've ever had.",
        "Absolutely fantastic service!",
        "I am not satisfied with the quality.",
        "Great job, highly recommend!",
        "Terrible, I will never buy this again."
    ],
    'label': ['positive', 'negative', 'positive', 'negative', 'positive', 'negative']
}

df = pd.DataFrame(data)

# Step 2: Data Preprocessing
# Download stopwords
nltk.download('stopwords')

def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    text = ' '.join(word for word in text.split() if word not in stop_words)
    return text

# Apply preprocessing
df['cleaned_feedback'] = df['feedback'].apply(preprocess_text)

# Step 3: Feature Extraction
# Initialize CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['cleaned_feedback'])

# Labels
y = df['label']

# Step 4: Split the Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train the Model
# Initialize the model
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

# Step 6: Make Predictions
y_pred = model.predict(X_test)

# Step 7: Evaluate the Model
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Step 8: Use the Model for New Feedback
def classify_feedback(feedback):
    cleaned_feedback = preprocess_text(feedback)
    features = vectorizer.transform([cleaned_feedback])
    prediction = model.predict(features)
    return prediction[0]

# Test the model with new feedback
new_feedback = "I am very happy with the service!"
result = classify_feedback(new_feedback)
print(f"The feedback is: {result}")
