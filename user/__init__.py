from flask import Flask

app = Flask(__name__, template_folder='templates')

import user.db.model
import user.crud.user_crud
import user.crud.invalid_route