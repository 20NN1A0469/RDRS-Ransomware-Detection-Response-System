from app.core.scoring import calculate_score


result = calculate_score(
    rapid_encryption=True,
    mass_rename=True,
    high_entropy=True
)

print(result)