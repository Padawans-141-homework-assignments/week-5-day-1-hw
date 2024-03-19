from flask import Flask, request

app = Flask(__name__)

#the details/model of the flask app
ps_console_generation = {
    1 : {
        'name' : 'PlayStation',
        'price' : 399,
        'global-release-date' : 1995
    },
    2 : {
        'name' : 'PlayStation 2',
        'price' : 299,
        'global-release-date' : 2000
    },
    3 : {
        'name' : 'PlayStation 3',
        'price' : 499,
        'global-release-date' : 2006
    },
    4 : {
        'name' : 'PlayStation 4',
        'price' : 400,
        'global-release-date' : 2013
    },
    5 : {
        'name' : 'PlayStation 5',
        'price' : 500,
        'global-release-date' : 2020
    }
}

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

app.run()