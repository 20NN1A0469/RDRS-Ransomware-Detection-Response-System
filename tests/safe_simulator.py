from pathlib import Path
import os


SANDBOX = Path("data/sandbox")


def create_test_files(count=30):

    SANDBOX.mkdir(
        parents=True,
        exist_ok=True
    )

    for i in range(count):

        file_path = (
            SANDBOX /
            f"test_file_{i}.txt"
        )

        file_path.write_text(
            "This is a safe RDRS test file.\n"
            * 10
        )


def simulate_suspicious_activity():

    files = list(
        SANDBOX.glob("test_file_*.txt")
    )

    for file_path in files:

        random_data = os.urandom(4096)

        file_path.write_bytes(random_data)

        new_path = file_path.with_suffix(".locked")

        file_path.rename(new_path)

        print(
            f"Simulated activity: "
            f"{file_path.name} -> {new_path.name}"
        )


if __name__ == "__main__":

    create_test_files(30)

    simulate_suspicious_activity()

    print("Safe simulation completed.")