import yaml
from pathlib import Path


CONFIG_PATH = Path("config.yaml")


def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


if __name__ == "__main__":
    config = load_config()

    print("RDRS Configuration Loaded")
    print("-------------------------")

    print("Monitor paths:")
    print(config["monitor"]["paths"])

    print("Window:")
    print(config["monitor"]["window_seconds"], "seconds")

    print("Modified file threshold:")
    print(config["thresholds"]["modified_files"])

    print("Entropy threshold:")
    print(config["thresholds"]["entropy"])

    print("Simulation mode:")
    print(config["response"]["simulation_mode"])