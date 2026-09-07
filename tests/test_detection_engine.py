from app.detectors.detection_engine import DetectionEngine


engine = DetectionEngine(window_seconds=60)


for i in range(25):

    engine.add_event({
        "event_type": "MODIFY",
        "file_path": f"file_{i}.txt"
    })


for i in range(15):

    engine.add_event({
        "event_type": "RENAME",
        "file_path": f"file_{i}.locked",
        "extension_changed": True
    })


print(engine.get_statistics())