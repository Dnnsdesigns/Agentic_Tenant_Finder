class TenantProfile:
    def __init__(self, name, rental_history, credit_score, employment_status, references, budget, features):
        self.name = name
        self.rental_history = rental_history
        self.credit_score = credit_score
        self.employment_status = employment_status
        self.references = references
        self.budget = budget
        self.features = features
        self.score = 0

    def calculate_score(self):
        # Scoring algorithm based on rental history, credit score, and employment status
        self.score = (len(self.rental_history) * 2) + (self.credit_score / 100) + (len(self.employment_status) * 1.5)
        return self.score
