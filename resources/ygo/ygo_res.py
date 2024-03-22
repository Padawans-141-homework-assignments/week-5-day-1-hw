from model import fav_ygo_cards

from flask.views import MethodView

from uuid import uuid4

from schemas import ygoSchema

from . import bpygo

@bpygo.route('/ygo')
class ygoResourceList(MethodView):
    
    #converts objects into a JSON response
    @bpygo.response(200, ygoSchema(many=True))
    #GET for the generations resource
    def get(self):
        #try to grab a list of the values
        try:
            return list(fav_ygo_cards.values())
        #spit out error if there is none
        except:
            return {'err':'no dictionary could be found'}
    
    #converts objects into a JSON argument to be passed into the method
    @bpygo.arguments(ygoSchema)
    @bpygo.response(201, ygoSchema)
    #POST for the generations resource
    def post(self, data):
        try:
            #adds the new data into the dictionary
            fav_ygo_cards[data["name"]] = data
        except:
            #returns error if it happens
            return {'error' : 'problem adding new requsest to the dictionary'}
        
        #returns success
        return {'Information added successfully' : f'{fav_ygo_cards[data["name"]]}'}
    
@bpygo.route('/ygo/<int:id>')
class ygoResource(MethodView):
    
    #creates another object to be placed into the method as an argument
    @bpygo.arguments(ygoSchema)
    #PUT for the generations resource
    def put(self, data, id):
        #if the given endpoint is in the dictionary
        if id in fav_ygo_cards:
            #assign the given endpoint to the new data
            fav_ygo_cards[id] = data
            #return confirmation of update
            return{'confirmation' : f'Data: {fav_ygo_cards[id]} added successfully.'}
        else:
            #return confirmation of user error
            return {'error': 'provided enpoint id doesn\'t exist in the dictionary.'}
    
    #@bpgen.arguments(genSchema)
    def delete(self,id):
        #if the given id endpoint exists in the dictionary
        if id in fav_ygo_cards:
            #keep track of the to be deleted info
            deleted_id_info = fav_ygo_cards[id]
            #deletes the info at the given id
            del fav_ygo_cards[id]
            #returns confirmation of deletion
            return {'Confirmation' : f'Info: {deleted_id_info} deleted successfully.'}
        else:
            #return confirmation of user error
            return {'error' : 'Specified endpoint id doesn\'t exist.'}