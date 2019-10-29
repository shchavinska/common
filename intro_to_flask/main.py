from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/vegetables')
def vegetables():
    list_of_vegetables = ['beans', 'carrot', 'beetroot', 'cucumber']
    return render_template('vegetables.html', vegetables=list_of_vegetables)


@app.route('/fruits')
def fruits():
    list_of_fruits = ['melon', 'apple', 'strawberry', 'grape']
    return render_template('fruits.html', fruits=list_of_fruits)


if __name__ == "__main__":
    app.run(debug=True)

