from flask import Flask

def create_app(test_config=None):
    app= Flask(__name__)
    app.secret_key='hesdakjsnkmnsdaskjd123'

    from .urlshort import bp
    app.register_blueprint(bp)

    return app
