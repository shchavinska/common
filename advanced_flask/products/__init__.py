from flask import Blueprint, render_template, request, session, abort
import uuid


products = [{
    'id':'1',
    'name': 'Milk',
    'description': 'Something white',
    'img_name': '...',
    'price': '2$'
},{
    'id': '2',
    'name': 'Cola',
    'description': 'Something black',
    'img_name': '...',
    'price': '1$'
}]


blueprint_product = Blueprint('products', __name__, template_folder='templates', static_folder='static')


@blueprint_product.route('/')
def all_products():
    price = request.args.get('price')
    res = []
    if price:
        for product in products:
            if product['price'] == price:
                res.append(product)
    else:
        res = products

    for product in res:
        if session.get('product' + product['id']):
            product['used'] = "clicked"

    return render_template('all_products.html', products=res)


@blueprint_product.route('/<id>')
def get_product_id(id):
    for product in products:
        if product['id'] == id:
            session['product' + id] = True
            return render_template('product.html', product=product)
    abort(404)


@blueprint_product.route('/add', methods=['GET', 'POST'])
def add_product():
    new = {}
    if request.method == 'POST':
        name = request.form.get('Name')
        description = request.form['Description']
        price = request.form['Price']
        image = request.files['Image']
        image.save('products/static/' + name + '.png')
        new['id'] = uuid.uuid4().hex
        new['name'] = name
        new['description'] = description
        new['img_name'] = name
        new['price'] = price
        products.append(new)

    return render_template('add_product.html')

