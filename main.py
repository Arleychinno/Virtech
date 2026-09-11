import flask
import random
import string
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>THIS IS A WEBSITE TO KNOW SOMETHING NEW ABOUT TECHNOLOGY!</h1> <a href="/random_fact">View a random fact!</a>'

@app.route("/random_fact")
def facts():
    facts_list = [
        "Kebanyakan orang yang menderita kecanduan teknologi mengalami stres yang kuat ketika mereka berada di luar area jangkauan jaringan atau tidak dapat menggunakan perangkat mereka",
        "Menurut sebuah studi yang dilakukan pada tahun 2018, lebih dari 50% orang berusia 18 hingga 34 tahun menganggap diri mereka bergantung pada ponsel pintar mereka.",
        "Elon Musk mengklaim bahwa jejaring sosial dirancang untuk membuat kita tetap berada di dalam platform, sehingga kita menghabiskan waktu sebanyak mungkin untuk melihat konten"
    ]
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/pw_generate")
def password():
    characters = string.ascii_letters + string.digits + string.punctuation
    generated_password = ''.join(random.choice(characters) for i in range(12))

    return f'<p>Password kamu: <b>{generated_password}</b></p>'
    
@app.route("/coin_flip")
def coin():
    result = random.choice(["Heads", "Tails"])

    return f'<p>Hasil: <b>{result}</b></p>'

app.run(debug=True)
