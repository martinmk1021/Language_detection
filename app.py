#!/usr/bin/env python
# coding: utf-8

# In[5]:


from flask import Flask, request, jsonify, render_template_string
import pickle
import re  # Importing regular expressions for text processing

# Load the saved model
with open('model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

app = Flask(__name__)  # Fixing the app name with '__name__'

# Function to clean the input text
def clean_text(text):
    # Remove numbers and special characters, keeping letters from all languages
    cleaned_text = re.sub(r'[^\w\s]', '', text)  # Remove special characters
    cleaned_text = re.sub(r'\d+', '', cleaned_text)  # Remove digits
    return cleaned_text.strip()  # Remove leading/trailing whitespace

# HTML template with embedded CSS and JavaScript for AJAX
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Language Detection</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }

        .container {
            max-width: 600px;
            margin: 0 auto;
            background: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        h1 {
            text-align: center;
        }

        form {
            display: flex;
            flex-direction: column;
        }

        input[type="text"] {
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        input[type="submit"] {
            background-color: #28a745;
            color: white;
            border: none;
            padding: 10px;
            cursor: pointer;
            border-radius: 5px;
        }

        input[type="submit"]:hover {
            background-color: #218838;
        }

        #result {
            margin-top: 20px;
            font-size: 1.2em;
            color: #333;
        }
    </style>
    <script>
        function submitForm(event) {
            event.preventDefault(); // Prevent the default form submission
            var text = document.getElementById('text-input').value;

            // Make an AJAX request to the /predict endpoint
            fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ text: text })
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('result').innerText = 'Predicted Language: ' + data['Predicted Language'];
            })
            .catch(error => {
                console.error('Error:', error);
                document.getElementById('result').innerText = 'Error occurred during prediction.';
            });
        }
    </script>
</head>
<body>
    <div class="container">
        <h1>Language Detection</h1>
        <form onsubmit="submitForm(event)">
            <input type="text" id="text-input" name="text" placeholder="Enter text for language detection" required>
            <input type="submit" value="Detect Language">
        </form>
        <div id="result"></div> <!-- Placeholder for the prediction result -->
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Get JSON data from the request
    text = data['text']  # Extract the text
    cleaned_text = clean_text(text)  # Clean the input text
    prediction = loaded_model.predict([cleaned_text])  # Use the cleaned text for prediction
    return jsonify({'Predicted Language': prediction[0]})

if __name__ == '__main__':  # Fixing the main condition
    app.run(port=5000)


# In[ ]:




