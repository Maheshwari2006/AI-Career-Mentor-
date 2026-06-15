class RoadmapGenerator:

    ROADMAPS = {

        "tensorflow": [
            "Lean TensorFlow Basics",
            "Build Neural Networks",
            "Practice Image Classification"
        ],

        "pytorch": [
            "Learn PyTorch Fundamentals",
            "Build Deep Learning Models",
            "Implement CNN Projects"
        ],

        "opencv": [
            "Learn OpenCV Basics",
            "Image Processing",
            "Computer Vision Projects"
        ],

        "sql": [
            "SQL Fundamentals",
            "Joins & Queries",
            "Database Projects"
        ],

        "aws": [
            "AWS Cloud Basics",
            "EC2 & S3",
            "Deploy ML Applications"
        ],

        "docker": [
            "Docker Basics",
            "Containerization",
            "Deploy Flask Apps"
        ]
    }

    def __init__(self, missing_skills):

        self.missing_skills = missing_skills

    def generate(self):

        roadmap = {}

        for skill in self.missing_skills:

            roadmap[skill] = (
                self.ROADMAPS.get(
                    skill.lower(),
                    ["Learn Fundamentals"]
                )
            )

        return roadmap