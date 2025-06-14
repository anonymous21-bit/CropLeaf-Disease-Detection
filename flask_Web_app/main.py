from website import create_app
from flask import Flask, Blueprint, redirect,  url_for, render_template 


app = create_app()


if __name__=='__main__':
    app.run(debug=True)