class BackgroundCheckService:
    def check(self, tenant):
        # Simulated background check
        return {
            "criminal_history": "Clean",
            "eviction_records": "None",
            "credit_report": tenant.credit_score
        }
