import os
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {"pdf", "docx"}

def allowed_file(filename):
    return (
        "." in filename and
        filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )

def save_file(file, upload_folder):
    filename = secure_filename(file.filename)

    filepath = os.path.join(
        upload_folder,
        filename
    )

    file.save(filepath)

    return filepath