from flask import Flask

def create_app():
    app = Flask(__name__)

    from .views import views
   #from .data import data 
    from .query import query
    from .webmap import webmap
    from .views import team

    app.register_blueprint(views, url_prefix='/')
   # app.register_blueprint(data, url_prefix='/')
    app.register_blueprint(query, url_prefix='/')
    app.register_blueprint(webmap, url_prefix='/')
    app.register_blueprint(team, url_prefix='/')

    return app
