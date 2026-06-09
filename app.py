from flask import Flask
from config import Config

from flask_login import (
    LoginManager,
    login_required
)

from database.models import db
from database.models.user import User
from database.models.resume import Resume

from routes.auth_routes import auth_bp
from routes.resume_routes import resume_bp

def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    login_manager = LoginManager()

    login_manager.init_app(app)

    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    app.register_blueprint(auth_bp)
    app.register_blueprint(resume_bp)

    with app.app_context():
        db.create_all()

    @app.route("/")
    def home():
        return """
        <h2>AI Career Mentor</h2>
        <a href='/register'>Register</a>
        <br><br>
        <a href='/login'>Login</a>
        """

    @app.route("/dashboard")
    @login_required
    def dashboard():

        from flask import render_template

        return render_template(
            "dashboard.html"
        )

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)