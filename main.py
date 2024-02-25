from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length=12, capitalize=False):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = lowercase_letters + digits + special_characters
    if capitalize:
        all_characters += uppercase_letters

    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    length = int(request.form['length'])
    capitalize = 'capitalize' in request.form
    password = generate_password(length, capitalize)
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)