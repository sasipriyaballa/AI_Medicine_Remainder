import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("dataset/medicine_log.csv")

# Convert time to hour
data["hour"] = data["time"].str.split(":").str[0].astype(int)

# Encode categorical columns
le_medicine = LabelEncoder()
le_condition = LabelEncoder()
le_status = LabelEncoder()

data["medicine_name"] = le_medicine.fit_transform(data["medicine_name"])
data["condition"] = le_condition.fit_transform(data["condition"])
data["status"] = le_status.fit_transform(data["status"])

# Features
X = data[["medicine_name","age","condition","hour"]]

# Target
y = data["status"]

# Split dataset
X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.2,random_state=42
)

# Train model
model = RandomForestClassifier(n_estimators=200)
model.fit(X_train,y_train)

# Accuracy
pred = model.predict(X_test)
accuracy = accuracy_score(y_test,pred)

print("Model Accuracy:",accuracy)

# Save model
pickle.dump(model,open("model.pkl","wb"))
pickle.dump(le_medicine,open("medicine_encoder.pkl","wb"))
pickle.dump(le_condition,open("condition_encoder.pkl","wb"))
pickle.dump(le_status,open("status_encoder.pkl","wb"))

print("Model saved successfully")