from flask import request, jsonify
from flask_jwt_extended import create_access_token, get_jwt, get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager

from flask.views import MethodView
from flask_smorest import abort

from app import app
from models.signin_model import make_usr_model
from schemas import make_usr_schema
from . import bpusr

#decodes the JWT with this key. If the response doesn't match the key access is denied to the user.
app.config["JWT_SECRET_KEY"] = "This is used to decode the JWT"

#Inherits the flask instantiation into the JWTManager class
jwt = JWTManager(app)

#changes the missing authorization response to something I chose
@jwt.unauthorized_loader
def custom_message(error_msg):
    return jsonify({
        "error" : "You either didn't login or your JWT expired. Please login again :)"
    }), 401

#logs in the user
@app.post('/login')
def usr_login():
    
    #grabs the user request
    usr_data = request.get_json()

    #grabs the username info from the user data
    username = usr_data['username']

    #queries the table and filters it where the username is username and
    #grabs the first applicable row.
    user = make_usr_model.query.filter_by(username = username).first()

    #if there is a user with a name equal to the users request and
    #the user provided password matches the hased password
    if user and user.check_usr_password(usr_data['password']):
        #creates an access token where the JWT header is the users database id
        usr_token = create_access_token(identity=username)
        return {'access-token' : usr_token}, 201
    
    #notifies if information is wrong.
    abort(400, message = 'Either username or password is invalid.')

#logs out the user
@bpusr.post('/logout')
def usr_logout():

    #confirms successfull logout
    response = jsonify({'confirmation' : "you have logged out successfully."})
    #deletes any created cookies that were created
    unset_jwt_cookies(response)
    return response

#creates route for the signup page
@bpusr.route('/signup')
class mkusrResourceList(MethodView):

    #grabs user api request
    @bpusr.response(200, make_usr_schema(many=True))
    #GET the contents of the user table
    def get(self):
        #querys all the contents in the user table
        try:
            return make_usr_model.query.all()
        except:
            abort(400, message = 'Couldn\'t return the information from the database.')

    #converts incoming request into an argument for the method
    @bpusr.arguments(make_usr_schema)
    @bpusr.response(201, make_usr_schema)
    #POST for the users table resource
    def post(self, data):

        try:
            #assigns the make user model class for future reference
            mkusr = make_usr_model()
            #forms the incoming api request data
            mkusr.from_usr(data)
            #saves the user data into the database
            mkusr.save_usr()
            return{"Confirmation" : "Your user information was successfully created"}
        except:
            #informs of errors
            abort(400, message = 'There was a problem when entering your information into the database.')

@bpusr.route('/signup/<int:id>')
class mkusrResource(MethodView):

    #Creates readable json from passed in user request as 'data'
    @bpusr.arguments(make_usr_schema)
    #PUT for the signin resource
    def put(self, data, id):

        user = make_usr_model.query.get(id)
        print(user)

        try:
            #forms the data request
            user.from_usr(data)
            #saves the data to the database
            user.save_usr()
            return {"confirmation" : "user has been updated successfully."}
        except:
            #informs of errors
            #abort(400, message = "There is no user with that id in the database.")
            return {"error" : f'{user.from_usr(data)}'}

    def delete(self, id):

        #querys the database at the id location
        user = make_usr_model.query.get(id)

        #if there is a user with that id
        if user:
            #delete that user at that id location
            user.del_usr()
            return {'Confirmation' : 'User is now deleted from the database'}
        else:
            #inform of error
            abort(400, message = 'User with that ID not found in the database')
