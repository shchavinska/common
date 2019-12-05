from flask import Flask, render_template
from products import blueprint_product
from supermarkets import blueprint_supermarket


app = Flask(__name__)
app.register_blueprint(blueprint_product, url_prefix='/product')
app.register_blueprint(blueprint_supermarket, url_prefix='/supermarket')
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.route('/')
def go_home():
    return render_template('home.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == "__main__":
    app.run(debug = True)
