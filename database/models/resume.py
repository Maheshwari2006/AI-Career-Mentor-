from database.models import db


class Resume(db.Model):

    __tablename__ = "resumes"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        nullable=False
    )

    file_name = db.Column(
        db.String(255)
    )

    file_path = db.Column(
        db.String(255)
    )

    ats_score = db.Column(
        db.Float,
        default=0
    )

    uploaded_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )