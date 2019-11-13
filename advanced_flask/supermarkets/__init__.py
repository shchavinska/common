from flask import Blueprint, render_template, request, session, abort
import uuid


supermarkets = [{
    'id':'1',
    'name': 'Fora',
    'location': 'Kyiv',
    'img_name': '...'
},{
    'id': '2',
    'name': 'Silpo',
    'location': 'Odesa',
    'img_name': '...'
},]


blueprint_supermarket = Blueprint('supermarkets', __name__, template_folder='templates', static_folder='static')


@blueprint_supermarket.route('/')
def all_supermarkets():
    location = request.args.get('location')
    res = []
    if location:
        for supermarket in supermarkets:
            if supermarket['location'] == location:
                res.append(supermarket)
    else:
        res = supermarkets

    for supermarket in res:
        if session.get('supermarket' + supermarket['id']):
            supermarket['used'] = "clicked"

    return render_template('all_supermarkets.html', supermarkets=res)


@blueprint_supermarket.route('/<id>')
def get_supermarket_id(id):
    for supermarket in supermarkets:
        if supermarket['id'] == id:
            session['supermarket' + id] = True
            return render_template('supermarket.html', supermarket=supermarket)
    abort(404)


@blueprint_supermarket.route('/add', methods=['GET', 'POST'])
def add_supermarket():
    new = {}
    if request.method == 'POST':
        name = request.form.get('Name')
        location = request.form['Location']
        image = request.files['Image']
        image.save('supermarkets/static/' + name + '.png')
        new['id'] = uuid.uuid4().hex
        new['name'] = name
        new['location'] = location
        new['img_name'] = name
        supermarkets.append(new)

    return render_template('add_supermarket.html')
