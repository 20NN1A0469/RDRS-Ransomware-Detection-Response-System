from datetime import datetime, timezone

from app.database.database import SessionLocal
from app.database.models import Alert, Incident


def create_incident(score, level, reasons, suspect_process=None):

    db = SessionLocal()

    try:

        reason_text = ", ".join(reasons)

        alert = Alert(
            severity=level,
            message=reason_text,
            timestamp=datetime.now(timezone.utc)
        )

        db.add(alert)

        incident = Incident(
            severity=level,
            score=score,
            suspect_process=suspect_process,
            status="OPEN",
            timestamp=datetime.now(timezone.utc)
        )

        db.add(incident)

        db.commit()

        db.refresh(incident)

        print(f"Incident created: INC-{incident.id:04d}")

        return incident.id

    finally:

        db.close()