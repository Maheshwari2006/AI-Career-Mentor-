import pickle


class CareerPredictor:

    def __init__(self):

        self.model = pickle.load(
            open(
                "ml/career_model.pkl",
                "rb"
            )
        )

        self.vectorizer = pickle.load(
            open(
                "ml/vectorizer.pkl",
                "rb"
            )
        )

        self.encoder = pickle.load(
            open(
                "ml/encoder.pkl",
                "rb"
            )
        )

    def predict(self, skills):

        skills_text = " ".join(
            skills
        )

        vector = self.vectorizer.transform(
            [skills_text]
        )

        prediction = self.model.predict(
            vector
        )

        career = (
            self.encoder.inverse_transform(
                prediction
            )[0]
        )

        confidence = max(
            self.model.predict_proba(
                vector
            )[0]
        )

        return {

            "career": career,

            "confidence":
            round(
                confidence * 100,
                2
            )
        }