from flask.views import MethodView
from uuid import uuid4

from schemas import genSchema
from . import bpgen
from model import ps_console_generation

#creates route for the new class
@bpgen.route('/gen')
class genResourceList(MethodView):
    
    #converts objects into a JSON response
    @bpgen.response(200, genSchema(many=True))
    #GET for the generations resource
    def get(self):
        #try to grab a list of the values
        try:
            return list(ps_console_generation.values())
        #spit out error if there is none
        except:
            return {'err':'no dictionary could be found'}
    
    #converts objects into a JSON argument to be passed into the method
    @bpgen.arguments(genSchema)
    @bpgen.response(201, genSchema)
    #POST for the generations resource
    def post(self, data):

        try:
            #adds the new data into the dictionary
            ps_console_generation[data["name"]] = data
        except:
            #returns error if it happens
            return {'error' : 'problem adding new requsest to the dictionary'}
        
        #returns success
        return {'Information added successfully' : f'{ps_console_generation[data["name"]]}'}
        
        
@bpgen.route('/gen/<int:id>')
class genResource(MethodView):
    
    #creates another object to be placed into the method as an argument
    @bpgen.arguments(genSchema)
    #PUT for the generations resource
    def put(self, data, id):

        #if the given endpoint is in the dictionary
        if id in ps_console_generation:
            #assign the given endpoint to the new data
            ps_console_generation[id] = data
            #return confirmation of update
            return{'confirmation' : f'Data: {ps_console_generation[id]} added successfully.'}
        else:
            #return confirmation of user error
            return {'error': 'provided enpoint id doesn\'t exist in the dictionary.'}
    
    #@bpgen.arguments(genSchema)
    def delete(self,id):

        #if the given id endpoint exists in the dictionary
        if id in ps_console_generation:
            #keep track of the to be deleted info
            deleted_id_info = ps_console_generation[id]
            #deletes the info at the given id
            del ps_console_generation[id]
            #returns confirmation of deletion
            return {'Confirmation' : f'Info: {deleted_id_info} deleted successfully.'}
        else:
            #return confirmation of user error
            return {'error' : 'Specified endpoint id doesn\'t exist.'}
        
