from flask import Flask, render_template, request
import json
import nltk
from nltk.tokenize import TreebankWordTokenizer

# Download necessary NLTK resources
nltk.download('punkt', quiet=True)  # Quiet mode to suppress output
nltk.download('punkt_tab', quiet=True)  # Quiet mode to suppress output

app = Flask(__name__)

# Load the emoji dictionary
with open('data/emoji_dict.json', 'r', encoding='utf-8') as f:
    emoji_data = json.load(f)

# Create a quick access dictionary for emojis by aliases and tags
emoji_dict = {}
for emoji in emoji_data:
    for alias in emoji['aliases']:
        emoji_dict[alias] = emoji['emoji']
    for tag in emoji['tags']:
        emoji_dict[tag] = emoji['emoji']
    emoji_dict[emoji['description']] = emoji['emoji']

# Initialize the tokenizer globally
tokenizer = TreebankWordTokenizer()

def text_to_emojis(text):
    # Tokenize the input text using TreebankWordTokenizer
    words = tokenizer.tokenize(text)
    emoji_representation = []
    
    # Join words back to form the original text for full phrase matching
    original_text = ' '.join(words)

    # Check for the full emoji name in the dictionary first
    if original_text in emoji_dict:
        return emoji_dict[original_text]  # Return the emoji for the full phrase

    # If no full match, check individual words
    for word in words:
        word_lower = word.lower()  # Normalize to lowercase
        if word_lower in emoji_dict:
            emoji_representation.append(emoji_dict[word_lower])
        else:
            emoji_representation.append(word)

    return ' '.join(emoji_representation)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    text = request.form['text']
    emoji_text = text_to_emojis(text)
    return render_template('result.html', emoji_text=emoji_text)

if __name__ == '__main__':
    app.run(debug=True)
