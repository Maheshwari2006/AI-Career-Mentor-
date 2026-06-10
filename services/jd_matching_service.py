from nlp.skills_db import SKILLS


class JDMatcher:

    def __init__(self, resume_text, job_description):

        self.resume_text = resume_text.lower()
        self.job_description = job_description.lower()

    def matched_skills(self):

        matched = []

        for skill in SKILLS:

            if (
                skill.lower() in self.resume_text
                and
                skill.lower() in self.job_description
            ):
                matched.append(skill)

        return matched

    def missing_skills(self):

        missing = []

        for skill in SKILLS:

            if (
                skill.lower() not in self.resume_text
                and
                skill.lower() in self.job_description
            ):
                missing.append(skill)

        return missing

    def calculate_match_score(self):

        matched = len(
            self.matched_skills()
        )

        missing = len(
            self.missing_skills()
        )

        total_required = (
            matched + missing
        )

        if total_required == 0:
            return 0

        score = (
            matched /
            total_required
        ) * 100

        return round(
            score,
            2
        )

    def analyze(self):

        return {

            "match_score":
            self.calculate_match_score(),

            "matched_skills":
            self.matched_skills(),

            "missing_skills":
            self.missing_skills()
        }

