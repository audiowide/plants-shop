from masonite.routes import Route
from masonite.authentication import Auth

ROUTES = [
    Route.get("/", "WelcomeController@show"),
    
    # Blog
    Route.get("/blog", "BlogController@show"),
    Route.get("/blog/:id", "BlogController@show_one"),
    Route.get("/create-article", "BlogController@create"),
    
]

ROUTES += Auth.routes()