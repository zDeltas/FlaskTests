from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)


list_colors = ["rouge", "ecarlate", "vermeil", "jaune", "orange", "olive", "or", "gris", "brique", "blond", "blanc", "bleu", "vert", "violet"]

@app.route('/')
def index():
    return render_template('index.html', list_colors=list_colors)

@app.route('/output')
def suggestions():
    text = request.args.get('outData')

    list_color_output = []
    if text:
        for input_color in list_colors:
            if input_color.startswith(text):
                list_color_output.append(input_color)

    return render_template('output.html', outputs=list_color_output)

if __name__ == "__main__":
    app.run()