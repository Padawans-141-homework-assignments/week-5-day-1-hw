from models.ygo_model import ygo_Model

from flask.views import MethodView

from flask_smorest import abort

from schemas import ygoSchema

from . import bpygo

@bpygo.route('/ygo')
class ygoResourceList(MethodView):
    
    #converts objects into a JSON response
    @bpygo.response(200, ygoSchema(many=True))
    #GET for the generations resource
    def get(self):

        #returns a query of everthing in the current database
        try:
            return ygo_Model.query.all()
        #informs of error if needed
        except:
            abort(400, message = 'Couldn\'t return the information from the database')
    
    #converts objects into a JSON argument to be passed into the method
    @bpygo.arguments(ygoSchema)
    @bpygo.response(201, ygoSchema)
    #POST for the generations resource
    def post(self, data):

        try:
            #grants the user of the model for the generations class
            gen_layout = ygo_Model()
            #forms the passed in data
            gen_layout.from_ygo(data)
            #saves the data from above into the database
            gen_layout.save_ygo()
            return {'Confirmation' : 'Your data was successfully entered into the database'}
        except:
            #informs if an error shows up
            abort(400, message = 'There was a problem entering the information into the database.')
    
@bpygo.route('/ygo/<int:id>')
class ygoResource(MethodView):
    
    #creates another object to be placed into the method as an argument
    @bpygo.arguments(ygoSchema)
    #PUT for the generations resource
    def put(self, data, id):

        #uses the model to query the database for the given id
        user = ygo_Model.query.get(id)

        try:
            #forms the passed in data
            user.from_ygo(data)
            #saves the passed in data to the database
            user.save_ygo()
            return {"Confirmation" : "user has been updated successfully"}
        except:
            #informs if an error shows up
            abort(400, message = 'There is no user with that id in the database.')
    
    #@bpgen.arguments(genSchema)
    def delete(self,id):

        #querys the database at the given id location
        user = ygo_Model.query.get(id)

        #if something exists at that id endpoint
        if user:
            #delete the contents at that location
            user.del_ygo()
            return {'Confirmation' : 'User is now deleted from the database.'}
        else:
            #else inform the user of an error
            abort(400, message = 'User with that ID not found in the database')