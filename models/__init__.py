from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from .parent import *
from .volunteer import *
from .child import *
from .term import *
from .user import *
from .member import *
