import shutil
from pathlib import Path


def quarantine_file(
    file_path: str,
    incident_id: int
):

    source = Path(file_path)

    if not source.exists():
        raise FileNotFoundError(file_path)

    quarantine_dir = (
        Path("data")
        / "quarantine"
        / f"INC-{incident_id:04d}"
    )

    quarantine_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    destination = quarantine_dir / source.name

    shutil.copy2(
        source,
        destination
    )

    return str(destination)