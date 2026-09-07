from app.reports.report_generator import generate_json_report


file = generate_json_report(
    incident_id=1,
    score=95,
    severity="CRITICAL",
    reasons=[
        "Rapid encryption",
        "Mass rename",
        "High entropy"
    ],
    affected_files=50
)

print("Report created:", file)