import openai
from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)
openai.api_key = "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"


# Creating a route that has both GET and POST request methods
@app.route("/", methods=['GET', 'POST'])

def calculate():
    bmi=''
    if request.method == 'POST':
        Weight= request.form.get('question')
        response = openai.Completion.create(
            engine="text-davinci-003", 
            max_tokens=512,
            n=1,
            stop=None,  
            # model="text-davinci-003",
            prompt=Weight,
            temperature=0.6,
        )        
        text = response.choices[0].text
        html_text = text.replace('\n\n', '\n')
        bmi = html_text
    return render_template("index.html",bmi=bmi)