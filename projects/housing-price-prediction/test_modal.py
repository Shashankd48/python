import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the dataset from CSV
data = pd.read_csv('E:/Study/Programming-Languages/python/projects/housing-price-prediction/housing-data-set.csv')

# Convert categorical variables into numerical format using one-hot encoding
data = pd.get_dummies(data, columns=['mainroad', 'guestroom', 'basement', 'hotwaterheating',
                                     'airconditioning', 'prefarea', 'furnishingstatus'])

# Separate features and target variable
X = data.drop('price', axis=1)
y = data['price']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)
print("Training R-squared:", train_score)
print("Testing R-squared:", test_score)

# Make predictions on new data
new_data = pd.read_csv('E:/Study/Programming-Languages/python/projects/housing-price-prediction//new_data.csv')  # Load new dataset from CSV
new_data = pd.get_dummies(new_data, columns=['mainroad', 'guestroom', 'basement', 'hotwaterheating',
                                             'airconditioning', 'prefarea', 'furnishingstatus'])

# Ensure that the new dataset has the same columns as the training dataset
missing_cols = set(X.columns) - set(new_data.columns)
for col in missing_cols:
    new_data[col] = 0
new_data = new_data[X.columns]  # Reorder columns to match training data

# Make predictions
new_predictions = model.predict(new_data)
print("Predicted Prices for New Dataset:", new_predictions)
