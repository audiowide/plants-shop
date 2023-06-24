""" Article Model """

from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to, has_many


class Article(Model):
    """Article Model"""

    __fillable__ = ['title', 'slug','body', 'user_id', 'tag_id']
    
    @belongs_to('user_id', 'id')
    def user(self):
        from app.models.User import User
        return User
    
    @belongs_to('tag_id', 'id')
    def user(self):
        from app.models.Tag import Tag
        return Tag
    
    @has_many('comment_id', 'id')
    def comments(self):
        from app.models.Comment import Comment
        return Comment