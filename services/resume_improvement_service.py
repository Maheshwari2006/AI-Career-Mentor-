class ResumeImprovementService:

    def __init__(self, parsed_resume):

        self.parsed_resume = parsed_resume

    def analyze(self):

        suggestions = []

        # Skills

        if len(
            self.parsed_resume["skills"]
        ) < 10:

            suggestions.append(
                "Add more technical skills relevant to your target role."
            )

        # Projects

        if len(
            self.parsed_resume["projects"]
        ) < 2:

            suggestions.append(
                "Add more AI/ML projects to strengthen your portfolio."
            )

        # Experience

        if len(
            self.parsed_resume["experience"]
        ) == 0:

            suggestions.append(
                "Add internships, training, or practical experience."
            )

        # Education

        if len(
            self.parsed_resume["education"]
        ) == 0:

            suggestions.append(
                "Add your educational qualifications clearly."
            )

        # ATS Keywords

        important_keywords = [

            "tensorflow",
            "pytorch",
            "opencv",
            "docker",
            "aws",
            "sql",
            "machine learning"
        ]

        resume_skills = [

            skill.lower()

            for skill in
            self.parsed_resume["skills"]
        ]

        for keyword in important_keywords:

            if keyword not in resume_skills:

                suggestions.append(
                    f"Consider adding {keyword} to your skillset."
                )

        if not suggestions:

            suggestions.append(
                "Excellent Resume! No major improvements required."
            )

        return suggestions
