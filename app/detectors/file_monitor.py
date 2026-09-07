import time
from pathlib import Path

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from app.core.logging_config import get_logger


logger = get_logger()


class RDRSEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        if event.is_directory:
            return

        logger.info(f"FILE CREATED: {event.src_path}")
        print(f"[CREATE] {event.src_path}")

    def on_modified(self, event):
        if event.is_directory:
            return

        logger.info(f"FILE MODIFIED: {event.src_path}")
        print(f"[MODIFY] {event.src_path}")

    def on_deleted(self, event):
        if event.is_directory:
            return

        logger.info(f"FILE DELETED: {event.src_path}")
        print(f"[DELETE] {event.src_path}")

    def on_moved(self, event):
        if event.is_directory:
            return

        logger.info(
            f"FILE RENAMED: {event.src_path} -> {event.dest_path}"
        )

        print(
            f"[RENAME] {event.src_path} -> {event.dest_path}"
        )


def start_monitor(path: str):
    monitor_path = Path(path)

    if not monitor_path.exists():
        monitor_path.mkdir(parents=True, exist_ok=True)

    event_handler = RDRSEventHandler()

    observer = Observer()
    observer.schedule(
        event_handler,
        str(monitor_path),
        recursive=True
    )

    observer.start()

    logger.info(f"RDRS file monitor started: {monitor_path}")

    print(f"Monitoring: {monitor_path}")
    print("Press CTRL+C to stop.")

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nStopping monitor...")

        observer.stop()

    observer.join()


if __name__ == "__main__":
    start_monitor("data/sandbox")