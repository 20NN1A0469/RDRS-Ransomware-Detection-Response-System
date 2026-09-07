from app.core.incident_manager import create_incident


incident_id = create_incident(
    score=95,
    level="CRITICAL",
    reasons=[
        "Rapid encryption activity",
        "Mass file rename activity",
        "High file entropy"
    ],
    suspect_process="python.exe"
)

print("Created incident:", incident_id)