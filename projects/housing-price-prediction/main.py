import joblib
from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.model_selection import train_test_split

# Load the dataset
data = pd.read_csv('E:\Study\Programming-Languages\python\projects\housing-price-prediction\housing-data-set.csv')
# data = pd.get_dummies(data, columns=['Location'])

data = pd.get_dummies(data, columns=['area','bedrooms','bathrooms','stories','mainroad','guestroom','basement','hotwaterheating','airconditioning','parking','prefarea','furnishingstatus'])


X = data.drop('price', axis=1)
y = data['price']

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model to disk
joblib.dump(model, 'house_price_model.pkl')

# Load the model from disk
loaded_model = joblib.load('house_price_model.pkl')

# Make predictions with the loaded model
predictions = loaded_model.predict(X_test)

# Option 1: Print predictions directly
print("Predictions:", predictions)

# Option 2: Compare predictions with actual values
comparison = pd.DataFrame({'Actual': y_test, 'Predicted': predictions})
print(comparison)

# Option 3: Save predictions to a CSV file
comparison.to_csv('predictions.csv', index=False)
print("Predictions saved to predictions.csv")
