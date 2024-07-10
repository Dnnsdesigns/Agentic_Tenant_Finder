class LandlordAgent:
    def __init__(self, properties, tenants):
        self.matcher = TenantMatcher(properties, tenants)
        self.background_service = BackgroundCheckService()

    def get_recommendations(self):
        matches = self.matcher.match_tenants()
        recommendations = []
        for property, tenants in matches:
            for tenant in tenants:
                background_check = self.background_service.check(tenant)
                if background_check["criminal_history"] == "Clean" and background_check["eviction_records"] == "None":
                    recommendations.append((property, tenant, tenant.calculate_score()))
        return recommendations

    def schedule_viewing(self, tenant, property):
        # Simulate scheduling
        print(f"Scheduled viewing for {tenant.name} at {property.location}")
