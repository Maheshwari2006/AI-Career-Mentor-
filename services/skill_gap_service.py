class SkillGapAnalyzer:

    CAREER_SKILLS = {

        "AI Engineer": [
            "python",
            "machine learning",
            "deep learning",
            "tensorflow",
            "pytorch",
            "nlp",
            "opencv",
            "sql"
        ],

        "Data Scientist": [
            "python",
            "sql",
            "pandas",
            "numpy",
            "machine learning",
            "statistics",
            "tableau"
        ],

        "Data Analyst": [
            "sql",
            "excel",
            "power bi",
            "tableau",
            "python"
        ],

        "Full Stack Developer": [
            "html",
            "css",
            "javascript",
            "react",
            "nodejs",
            "mongodb"
        ]
    }

    def __init__(
        self,
        user_skills,
        target_career
    ):

        self.user_skills = [
            skill.lower()
            for skill in user_skills
        ]

        self.target_career = (
            target_career
        )

    def analyze(self):

        required_skills = (
            self.CAREER_SKILLS.get(
                self.target_career,
                []
            )
        )

        missing_skills = []

        for skill in required_skills:

            if skill not in self.user_skills:

                missing_skills.append(
                    skill
                )

        return {

            "career":
            self.target_career,

            "required_skills":
            required_skills,

            "missing_skills":
            missing_skills
        }