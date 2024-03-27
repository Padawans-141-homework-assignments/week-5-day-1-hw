from marshmallow import Schema,fields

#Schema for the console Generation model
class genSchema(Schema):
    db_id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Int(required=True)
    global_release_date = fields.Int(required=True)

#Schema for the card creation model
class ygoSchema(Schema):
    db_id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    attribute = fields.Str(required=True)
    level_rank_link_rating = fields.Int(required=True)
    type = fields.Str(required=True)
    card_type = fields.Str(required=True)
    atk = fields.Int(required=True)
    effect = fields.Str(required=True)
    
    summon_requirement = fields.Str(required=False)
    defense = fields.Int(required=False)

#Schema for creating a user
class make_usr_schema(Schema):
    db_id = fields.Str(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
