from flask import Flask
from config import Config

from database.models import db

from database.models.user import User
from database.models.resume import Resume

def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route("/")
    def home():
        return """
        <h1>AI Career Mentor</h1>
        <h3>Project Setup Successful</h3>
        """

    return app


app = create_app()

if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )