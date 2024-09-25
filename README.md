# Language Detection

## Project Overview
This project aims to detect 17 different languages, which include:

- Arabic
- Danish
- Dutch
- English
- French
- German
- Greek
- Hindi
- Italian
- Kannada
- Malayalam
- Portuguese
- Russian
- Spanish
- Swedish
- Tamil
- Turkish

The dataset is sourced from Kaggle and consists of **10,337** rows in total. The data is split into an **80-20** ratio, with **8,269** for training and **2,068** for testing.

## Model Training
The code for this project is executed using **Python** in **Google Colab**. The final model achieved an accuracy of **98.02%** on the test data. Additionally, the saved model was manually tested with five sentences for each language, achieving **100%** accuracy.

## Requirements
To run this project, the following libraries are required:
- `seaborn==0.12.2`
- `numpy==1.24.3`
- `pandas==2.0.3`
- `matplotlib==3.7.2`
- `scikit-learn==1.3.0`

You can install these packages using the command:
```bash
pip install -r requirements.txt

## Usage
To load the saved model, use the following code:

```python
import pickle

with open('model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

Use the model to predict the language of new text data.

## Contributing
Feel free to fork the repository and submit pull requests for any enhancements or bug fixes.

