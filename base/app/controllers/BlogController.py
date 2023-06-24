from masonite.controllers import Controller
from masonite.views import View


class BlogController(Controller):
    
    def show(self, view: View):
        return view.render("blog/show_all")
    
    def show_one(self, view: View, id: int):
        return view.render("blog/show_one")
    
    def create(self, view: View):
        return view.render("blog/create")
    
    # def store(self, view: View):
    #     return 