from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

# Password generator function
def random_number():
    number1 = str(random.randint(0,9))
    number2 = str(random.randint(0,9))
    number3 = str(random.randint(0,9))
    number4= str(random.randint(0,9))
    numbers = [number1, number2, number3, number4]
    final_number = "".join(numbers)
    return final_number

def random_strings():
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    final_letters = random.choice(letters) + random.choice(letters) + random.choice(letters) + random.choice(letters)+ random.choice(letters)
    return final_letters

def random_term():
    terms = [

    ]

def generate_password():
    pass
