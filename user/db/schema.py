from flask_marshmallow import Marshmallow, Schema
from marshmallow import fields
from user import app

# for serialize the user object
ma = Marshmallow(app)


class UserSchema(ma.Schema):
    id = fields.Integer()
    first_name = fields.String()
    last_name = fields.String()
    mail_id = fields.String()
    age = fields.Integer()
