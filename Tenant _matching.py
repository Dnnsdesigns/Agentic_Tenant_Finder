class Property:
    def __init__(self, location, budget, lease_terms, features):
        self.location = location
        self.budget = budget
        self.lease_terms = lease_terms
        self.features = features

class TenantMatcher:
    def __init__(self, properties, tenants):
        self.properties = properties
        self.tenants = tenants

    def match_tenants(self):
        matches = []
        for property in self.properties:
            matched_tenants = sorted(
                [tenant for tenant in self.tenants if self._is_match(tenant, property)],
                key=lambda x: x.calculate_score(),
                reverse=True
            )
            matches.append((property, matched_tenants))
        return matches

    def _is_match(self, tenant, property):
        return tenant.budget <= property.budget and all(feature in tenant.features for feature in property.features)
