from flask import Flask, redirect, url_for, render_template 

def create_app():
    app= Flask(__name__)
    app.config['SECRET_KEY'] ='anonymous21'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    return app