import alchemy.transmutation

print("=== Transmutation 1 ===")
print("Import transmutation module directly")
lead_to_gold: str = alchemy.transmutation.recipes.lead_to_gold()
print(f"Testing lead to gold: {lead_to_gold}")
