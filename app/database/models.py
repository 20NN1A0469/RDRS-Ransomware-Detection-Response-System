from datetime import datetime

from sqlalchemy import Column, Integer, String, Float, DateTime, Text

from app.database.database import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    event_type = Column(String)
    file_path = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)
    entropy = Column(Float, nullable=True)


class Process(Base):
    __tablename__ = "processes"

    id = Column(Integer, primary_key=True, index=True)
    pid = Column(Integer)
    name = Column(String)
    cpu_percent = Column(Float)
    memory_percent = Column(Float)
    executable = Column(Text, nullable=True)
    parent_pid = Column(Integer, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)


class Score(Base):
    __tablename__ = "scores"

    id = Column(Integer, primary_key=True, index=True)
    score = Column(Float)
    level = Column(String)
    reason = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)


class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    severity = Column(String)
    message = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)


class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    severity = Column(String)
    score = Column(Float)
    suspect_process = Column(String, nullable=True)
    status = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)