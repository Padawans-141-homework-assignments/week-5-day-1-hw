from marshmallow import Schema,fields

#Schema for the console Generation model
class genSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Int(required=True)
    global_release_date = fields.Int(required=True)

#Schema for the card creation model
class ygoSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    attribute = fields.Str(required=True)
    level_rank_link_rating = fields.Int(required=True)
    type = fields.Str(required=True)
    card_type = fields.Str(required=True)
    summon_requirement = fields.Str()
    ATK = fields.Int(required=True)
    DEF = fields.Int()
    effect = fields.Str(required=True)