from flask import Flask, session

app = Flask(__name__)
app.secret_key = "appSeculoPDV"

@app.route('/visits-counter/')
def visits():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1  # reading and updating session data
    else:
        session['visits'] = 1 # setting session data
    return "Total visits: {}".format(session.get('visits'))


@app.route('/session/')
def updating_session():
    res = str(session.items())

    cart_item = {'pineapples': '10', 'apples': '20', 'mangoes': '30'}
    item_selecionado = {'teclado':'20', 'monitor': '50polegadas'}

    if 'cart_item' in session:
        itens = session['cart_item']
        itens.update(item_selecionado)
        # session['cart_item']['apples'] = '300'
        # session['cart_item'].add(item_selecionado)
        session.modified = True
    else:
        session['cart_item'] = cart_item

    return res





app.run(use_reloader=True)