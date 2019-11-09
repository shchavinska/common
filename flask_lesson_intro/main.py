from flask import Flask, render_template
from utils import get_data

app = Flask(__name__)


@app.route('/')
def get_home_page():
    return render_template("home.html", data=get_data())


@app.route('/<item_id>')
def item(item_id):
    item = get_item_by_title(item_id)
    if item:
        return render_template("items.html", item=item, res=len(item["text"].split()))
    else:
        return render_template("not_found.html")


@app.route('/author')
def author():
    return render_template("author.html")


def get_item_by_title(item_title):
    for item in get_data():
        if item["title"] == item_title:
            return item


if __name__ == "__main__":
    app.run(debug=True)

