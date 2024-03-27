from flask.views import MethodView
from flask_smorest import abort
from flask_jwt_extended import jwt_required

from models.gen_model import gen_Model
from schemas import genSchema
from . import bpgen

#creates route for the new class
@bpgen.route('/gen')
class genResourceList(MethodView):

    #converts objects into a JSON response
    @bpgen.response(200, genSchema(many=True))
    #GET for the generations resource
    def get(self):
        #returns a query of everthing in the current database
        try:
            return gen_Model.query.all()
        #informs of error if needed
        except:
            abort(400, message = 'Couldn\'t return the information from the database')
    
    #requires the user JWT to add a console generation
    @jwt_required()
    #converts objects into a JSON argument to be passed into the method
    @bpgen.arguments(genSchema)
    @bpgen.response(201, genSchema)
    #POST for the generations resource
    def post(self, data):

        try:
            #grants the user of the model for the generations class
            gen_layout = gen_Model()
            #forms the passed in data
            gen_layout.from_gen(data)
            #saves the data from above into the database
            gen_layout.save_gen()
            return {'Confirmation' : 'Your data was successfully entered into the database'}
        except:
            #informs if an error shows up
            abort(400, message = 'There was a problem entering the information into the database.')
        
        
@bpgen.route('/gen/<int:id>')
class genResource(MethodView):
    
    #requires the user JWT to update a console generation
    @jwt_required()
    #creates another object to be placed into the method as an argument
    @bpgen.arguments(genSchema)
    #PUT for the generations resource
    def put(self, data, id):

        #uses the model to query the database for the given id
        user = gen_Model.query.get(id)

        try:
            #forms the passed in data
            user.from_gen(data)
            #saves the passed in data to the database
            user.save_gen()
            return {"Confirmation" : "console generation has been updated successfully"}
        except:
            #informs if an error shows up
            abort(400, message = 'There is no console with that id in the database.')

    #requires user JWT to delete console generation
    @jwt_required()
    #DELETE for the generations resource
    def delete(self,id):

        #querys the database at the given id location
        user = gen_Model.query.get(id)

        #if something exists at that id endpoint
        if user:
            #delete the contents at that location
            user.del_gen()
            return {'Confirmation' : 'Generation is now deleted from the database.'}
        else:
            #else inform the user of an error
            abort(400, message = 'Console with that ID not found in the database')

        
