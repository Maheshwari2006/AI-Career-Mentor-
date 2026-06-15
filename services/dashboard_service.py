class DashboardService:

    def __init__(self, parsed_resume):

        self.parsed_resume = parsed_resume

    def generate(self):

        total_skills = len(
            self.parsed_resume["skills"]
        )

        total_projects = len(
            self.parsed_resume["projects"]
        )

        total_experience = len(
            self.parsed_resume["experience"]
        )

        total_education = len(
            self.parsed_resume["education"]
        )

        career = "AI Engineer"

        return {

            "skills_count":
            total_skills,

            "projects_count":
            total_projects,

            "experience_count":
            total_experience,

            "education_count":
            total_education,

            "career":
            career
        }
