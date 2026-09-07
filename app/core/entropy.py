import math
from pathlib import Path


def calculate_entropy(file_path: str, sample_size: int = 65536) -> float:
    """
    Calculate Shannon entropy for the first 64 KB of a file.
    Returns a value between 0 and 8.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if not path.is_file():
        raise ValueError(f"Not a file: {file_path}")

    with open(path, "rb") as file:
        data = file.read(sample_size)

    if not data:
        return 0.0

    frequency = [0] * 256

    for byte in data:
        frequency[byte] += 1

    entropy = 0.0
    data_length = len(data)

    for count in frequency:
        if count == 0:
            continue

        probability = count / data_length
        entropy -= probability * math.log2(probability)

    return entropy