class InterviewGenerator:

    QUESTIONS = {

        "python": [
            "What are Python decorators?",
            "Difference between list and tuple?",
            "Explain OOP concepts in Python."
        ],

        "machine learning": [
            "What is overfitting?",
            "Explain supervised learning.",
            "What is bias vs variance?"
        ],

        "deep learning": [
            "What is a neural network?",
            "Explain CNN architecture.",
            "Difference between ML and DL?"
        ],

        "flask": [
            "What is Flask Blueprint?",
            "Explain Flask routing.",
            "Difference between Flask and Django?"
        ],

        "sql": [
            "What is a JOIN?",
            "Difference between WHERE and HAVING?",
            "What are primary keys?"
        ],

        "nlp": [
            "What is tokenization?",
            "Explain Named Entity Recognition.",
            "What is stemming?"
        ]
    }

    def __init__(self, skills):

        self.skills = skills

    def generate(self):

        questions = {}

        for skill in self.skills:

            if skill.lower() in self.QUESTIONS:

                questions[skill] = (
                    self.QUESTIONS[
                        skill.lower()
                    ]
                )

        return questions

