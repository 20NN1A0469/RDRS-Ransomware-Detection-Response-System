from collections import deque
from datetime import datetime, timedelta


class DetectionEngine:

    def __init__(self, window_seconds=60):

        self.window_seconds = window_seconds
        self.events = deque()

    def add_event(self, event):

        event["timestamp"] = datetime.now()

        self.events.append(event)

        self._remove_old_events()

    def _remove_old_events(self):

        cutoff = datetime.now() - timedelta(
            seconds=self.window_seconds
        )

        while self.events:

            if self.events[0]["timestamp"] >= cutoff:
                break

            self.events.popleft()

    def get_statistics(self):

        self._remove_old_events()

        modified = 0
        renamed = 0
        extension_changes = 0

        for event in self.events:

            event_type = event.get("event_type")

            if event_type == "MODIFY":
                modified += 1

            elif event_type == "RENAME":
                renamed += 1

                if event.get("extension_changed"):
                    extension_changes += 1

        return {
            "modified_files": modified,
            "renamed_files": renamed,
            "extension_changes": extension_changes,
            "total_events": len(self.events)
        }