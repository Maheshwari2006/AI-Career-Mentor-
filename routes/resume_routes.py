import os

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    flash,
    current_app,
    send_from_directory
)

from flask_login import (
    login_required,
    current_user
)

from werkzeug.utils import secure_filename

from flask import Blueprint, render_template

from database.models import db
from database.models.resume import Resume
from database.models.user import User

from services.file_service import (
    save_file,
    allowed_file
)

resume_bp = Blueprint(
    "resume",
    __name__
)


@resume_bp.route("/upload-resume",
                 methods=["GET", "POST"])
@login_required
def upload_resume():

    if request.method == "POST":

        if "resume" not in request.files:

            flash("No File Selected")

            return redirect(
                request.url
            )

        file = request.files["resume"]

        if file.filename == "":

            flash("Please Select a File")

            return redirect(
                request.url
            )

        if file and allowed_file(
                file.filename):

            filename = secure_filename(
                file.filename
            )

            filepath = os.path.join(
                current_app.config[
                    "UPLOAD_FOLDER"
                ],
                filename
            )

            file.save(filepath)

            resume = Resume(
                user_id=current_user.id,
                file_name=filename,
                file_path=filepath
            )

            db.session.add(resume)
            db.session.commit()

            flash(
                "Resume Uploaded Successfully"
            )

            return redirect(
                "/resume-history"
            )

    return render_template(
        "upload_resume.html"
    )


@resume_bp.route("/resume-history")
@login_required
def resume_history():

    resumes = Resume.query.filter_by(
        user_id=current_user.id
    ).all()

    return render_template(
        "resume_history.html",
        resumes=resumes
    )


@resume_bp.route(
    "/download/<filename>"
)
@login_required
def download_resume(filename):

    return send_from_directory(
        current_app.config[
            "UPLOAD_FOLDER"
        ],
        filename,
        as_attachment=True
    )
from services.file_service import (
    save_file
)

#Add Parse Route

from nlp.resume_parser import (
    ResumeParser
)
@resume_bp.route(
    "/parse-resume/<int:id>"
)
@login_required
def parse_resume(id):

    resume = Resume.query.get_or_404(
        id
    )

    parser = ResumeParser(
        resume.file_path
    )

    result = parser.parse()

    return render_template(
        "parsed_resume.html",
        result=result
    )