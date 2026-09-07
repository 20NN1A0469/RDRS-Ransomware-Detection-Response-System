import json
from pathlib import Path


def generate_json_report(
    incident_id,
    score,
    severity,
    reasons,
    affected_files
):

    report_dir = Path("reports")

    report_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    report = {

        "incident_id": f"INC-{incident_id:04d}",

        "severity": severity,

        "score": score,

        "reasons": reasons,

        "affected_files": affected_files

    }

    output_file = (
        report_dir /
        f"incident_{incident_id:04d}.json"
    )

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            report,
            file,
            indent=4
        )

    return str(output_file)