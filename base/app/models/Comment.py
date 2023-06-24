""" Comment Model """

from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to


class Comment(Model):
    """Comment Model"""

    __fillable__ = [ 'article_id', 'user_id', 'body']
    
    @belongs_to('user_id', 'id')
    def user(self):
        from app.models.User import User
        return User
    
    @belongs_to('article_id', 'id')
    def article(self):
        from app.models.Article import Article
        return Article
