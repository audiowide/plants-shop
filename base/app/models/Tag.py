""" Tag Model """

from masoniteorm.models import Model
from masoniteorm.relationships import has_many

class Tag(Model):
    """Tag Model"""

    __table__ = 'tags'
    __fillable__ = ["name"]
    
    
    @has_many('user_id', 'id')
    def users(self):
        from app.models.User import User
        return User