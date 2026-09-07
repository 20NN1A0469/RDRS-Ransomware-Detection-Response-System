from app.core.entropy import calculate_entropy


file_path = "data/sandbox/normal.txt"

entropy = calculate_entropy(file_path)

print("File:", file_path)
print("Entropy:", entropy)