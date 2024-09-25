#!/usr/bin/env python
# coding: utf-8

# In[3]:


from flask import Flask, request, jsonify, render_template
import pickle
import re  # Importing regular expressions for text processing

# Load the saved model
with open('model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

app = Flask(__name__)

# Function to clean the input text
def clean_text(text):
    # Remove numbers and special characters, keeping only letters and spaces
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
    return cleaned_text.strip()  # Remove leading/trailing whitespace

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']
    cleaned_text = clean_text(text)  # Clean the input text
    prediction = loaded_model.predict([cleaned_text])  # Use the cleaned text for prediction
    return jsonify({'Predicted Language': prediction[0]})

if __name__ == '__main__':
    app.run(port=5000)


# In[ ]:




