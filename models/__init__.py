from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from .term import *
from .user import *
from .member import *
from .parentchild import *
from .attendance import *
