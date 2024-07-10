from agent.property import Property
from agent.tenant_profile import TenantProfile
from agent.landlord_agent import LandlordAgent

def main():
    # Example usage
    properties = [Property("123 Main St", 1500, "1 year", ["pool", "gym"])]
    tenants = [
        TenantProfile("Alice", ["Previous Apartment"], 750, ["Software Engineer"], ["Reference1"], 1400, ["pool", "gym"]),
        TenantProfile("Bob", ["Previous House"], 680, ["Teacher"], ["Reference2"], 1600, ["gym"])
    ]

    agent = LandlordAgent(properties, tenants)
    recommendations = agent.get_recommendations()
    for property, tenant, score in recommendations:
        print(f"Property: {property.location}, Tenant: {tenant.name}, Score: {score}")

    agent.schedule_viewing(tenants[0], properties[0])

if __name__ == "__main__":
    main()
