from flask import Flask, request

from model import *

from uuid import uuid4

app = Flask(__name__)


#homepage - view
@app.route('/')
def root():
    return {
        'Welcome' : 'this is my flask app focused on the console generations for the PlayStation'
    }

#shows all generations [GET] - view
@app.route('/generations')
def all_gen():
    return {
        'all current generations' : list(ps_console_generation.values())
    }

#creates a new generation [POST] - view
@app.route('/gen', methods=["POST"])
def create():
    data = request.get_json()
    ps_console_generation[data['name']] = data
    return {
        'POST was intercepted' : ps_console_generation[data['name']]
    }

#updates a generation [PUT] - view
@app.route('/gen', methods=["PUT"])
def update():
    data = request.get_json()
    #creates list of the generation names
    console_names = [i['name'] for i in ps_console_generation.values()]

    update_key = None
    #finds the key that matches the name of the name in the PUT request
    for key, value in ps_console_generation.items():
        if value['name'] == data['name']:
            update_key = key
            break

    if data['name'] in console_names:
        #updates the value in the found key with the data from the PUT request
        ps_console_generation[update_key] = data
        return {
            'specified generation has been updated' : ps_console_generation[update_key]
        }
    return {
        'error' : 'There is no console generation of that name.'
    }

#deletes a generation [DELETE] -view
@app.route('/gen', methods=["DELETE"])
def delete():
    data = request.get_json()
    #creates list of the generation names
    console_names = [i['name'] for i in ps_console_generation.values()]

    update_key = None
    #finds the key that matches the name of the name in the PUT request
    for key, value in ps_console_generation.items():
        if value['name'] == data['name']:
            update_key = key
            break

    if data['name'] in console_names:
        #deletes the values associated with its key using the DELETE request
        del ps_console_generation[update_key]
        return {
            'specified generation has been erased from existence' : 'you can\'t get that data back :('
        }
    return {
        'error' : 'There is no console generation of that name.'
    }

################################################################################ Second Resource ################################################################################
#[GET] - grabs the information of the cards
@app.get('/ygo')
def get_card():
    try:
        return list(fav_ygo_cards.values()), 200
    except:
        return {'error' : 'Failed to gather card information'}, 400
    
#[POST] - creates information and puts it in the cards    
@app.post('/ygo')
def create_card():
    data = request.get_json()
    #v Checks if the new card matches names with any other pre-existing card v
    if data['name'] in fav_ygo_cards:
        #v Returns with error if it matches v
        return {'error', 'card with that name already exists'}, 400
    
    #creates unique id
    card_id = uuid4().hex
    #puts the new card in the object at the new id position
    fav_ygo_cards[card_id] = data
    #notifies the user the card is created
    return {'message' : 'Card successfully created',
            'card-id' : card_id}, 200

#[PUT] - finds card and updates it
@app.put('/ygo')
def update_card():
    data = request.get_json()

    #creates list of the card names
    card_names = [i['name'] for i in fav_ygo_cards.values()]

    update_key = None
    #finds the key that matches the name of the name in the PUT request
    for key, value in fav_ygo_cards.items():
        if value['name'] == data['name']:
            update_key = key
            break

    #checks if the sent object exists in the object
    if data['name'] in card_names:
        #assigns the new information over it if it does
        fav_ygo_cards[update_key] = data
        #notifies of the change
        return{'message' : f'card: {data["name"]} updated.'}, 201
    #outputs error if the update doesn't match to something
    return {'error' : 'No card with that name exists'}, 400

#[DELETE] - finds card and deletes it
@app.delete('/ygo')
def delete_card():
    data = request.get_json()
    card_id = data['name']

    #creates list of the card names
    card_names = [i['name'] for i in fav_ygo_cards.values()]

    update_key = None
    #finds the key that matches the name of the name in the PUT request
    for key, value in fav_ygo_cards.items():
        if value['name'] == data['name']:
            update_key = key
            break

    #checks if the requested card exists
    if data['name'] in card_names:
        #deletes the card it asks for if it does
        del fav_ygo_cards[update_key]
        return {'Card found' : f'Card: {card_id} deleted successfully.'}
    return {'error' : 'A card of the given details doesn\'t exist.'}

app.run()