import re
import PyPDF2
import spacy
import pytesseract

from pdf2image import convert_from_path
from nlp.skills_db import SKILLS

# Tesseract Path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# Load SpaCy Model
nlp = spacy.load("en_core_web_sm")


class ResumeParser:

    def __init__(self, pdf_path):

        self.pdf_path = pdf_path
        self.text = self.extract_text()

    def extract_text(self):

        text = ""

        # First try normal PDF extraction
        try:

            with open(self.pdf_path, "rb") as file:

                reader = PyPDF2.PdfReader(file)

                for page in reader.pages:

                    page_text = page.extract_text()

                    if page_text:
                        text += page_text + "\n"

        except Exception as e:

            print("PDF Reading Error:", e)

        # If no text found, use OCR
        if len(text.strip()) == 0:

            print("No text found. Using OCR...")

            try:

                pages = convert_from_path(
                    self.pdf_path,
                    poppler_path=r"C:\poppler\Library\bin\poppler-26.02.0\Library\bin"
                )

                for page in pages:

                    ocr_text = pytesseract.image_to_string(
                        page,
                        lang="eng"
                    )

                    text += ocr_text + "\n"

            except Exception as e:

                print("OCR Error:", e)

        print("\n===== EXTRACTED RESUME TEXT =====")
        print(text)
        print("=================================\n")

        return text.lower()

    def extract_skills(self):

        found_skills = []

        for skill in SKILLS:

            if skill.lower() in self.text:
                found_skills.append(skill)

        return sorted(list(set(found_skills)))

    def extract_education(self):

        education = []

        patterns = [
            r"b\.?tech",
            r"b\.?e",
            r"bachelor",
            r"m\.?tech",
            r"m\.?e",
            r"master",
            r"phd",
            r"diploma",
            r"engineering",
            r"computer science",
            r"information technology",
            r"electronics",
            r"electrical",
            r"mechanical",
            r"civil"
        ]

        for pattern in patterns:

            matches = re.findall(
                pattern,
                self.text,
                re.IGNORECASE
            )

            education.extend(matches)

        return sorted(list(set(education)))

    def extract_projects(self):

        projects = []

        lines = self.text.split("\n")

        for line in lines:

            if (
                "project" in line
                or "developed" in line
                or "built" in line
                or "created" in line
            ):
                projects.append(line.strip())

        return list(set(projects))

    def extract_experience(self):

        experience = []

        lines = self.text.split("\n")

        for line in lines:

            if (
                "intern" in line
                or "experience" in line
                or "worked" in line
                or "training" in line
            ):
                experience.append(line.strip())

        return list(set(experience))

    def parse(self):

        return {
            "skills": self.extract_skills(),
            "education": self.extract_education(),
            "projects": self.extract_projects(),
            "experience": self.extract_experience()
        }