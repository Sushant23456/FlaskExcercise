from flask import Flask, render_template, request
from wtforms import IntegerField, Form

app = Flask(__name__)

class InputForm(Form):
    number = IntegerField('Number')

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/result', methods=['GET'])
def result():
    number = request.args.get('number')
    if number:
        try:
            num = int(number)
            if num % 2 == 0:
                message = f"{num} is an even number."
            else:
                message = f"{num} is an odd number."
        except ValueError:
            message = "The provided value is not an integer."
    else:
        message = None
    return render_template('result.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
