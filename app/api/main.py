from fastapi import FastAPI
from datetime import datetime

from app.database.database import SessionLocal
from app.database.models import Event, Alert, Incident


app = FastAPI(
    title="RDRS API",
    description="Ransomware Detection and Response System",
    version="1.0.0"
)


@app.get("/health")
def health():

    return {
        "status": "healthy",
        "timestamp": datetime.utcnow()
    }


@app.get("/status")
def status():

    db = SessionLocal()

    try:

        incidents = db.query(Incident).filter(
            Incident.status == "OPEN"
        ).count()

        alerts = db.query(Alert).count()

        events = db.query(Event).count()

        return {
            "system": "RDRS",
            "status": "running",
            "open_incidents": incidents,
            "total_alerts": alerts,
            "total_events": events
        }

    finally:

        db.close()


@app.get("/alerts")
def get_alerts():

    db = SessionLocal()

    try:

        alerts = db.query(Alert).order_by(
            Alert.timestamp.desc()
        ).limit(50).all()

        return [
            {
                "id": alert.id,
                "severity": alert.severity,
                "message": alert.message,
                "timestamp": alert.timestamp
            }
            for alert in alerts
        ]

    finally:

        db.close()


@app.get("/events")
def get_events():

    db = SessionLocal()

    try:

        events = db.query(Event).order_by(
            Event.timestamp.desc()
        ).limit(100).all()

        return [
            {
                "id": event.id,
                "event_type": event.event_type,
                "file_path": event.file_path,
                "entropy": event.entropy,
                "timestamp": event.timestamp
            }
            for event in events
        ]

    finally:

        db.close()