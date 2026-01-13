"""
Conductor Application Core
Stage: observer

Responsibilities:
- keep server alive
- periodic heartbeat
- future hook for market scanner
"""

import time
import logging
from datetime import datetime


class ConductorApp:
    def __init__(self, config: dict):
        self.config = config
        self.stage = config.get("stage", "observer")
        self.interval = config.get("scanner", {}).get("interval_seconds", 60)

        logging.info("ConductorApp initialized")
        logging.info("Stage: %s", self.stage)
        logging.info("Heartbeat interval: %s sec", self.interval)

    def heartbeat(self) -> None:
        now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        logging.info("Heartbeat | stage=%s | time=%s UTC", self.stage, now)

    def run(self) -> None:
        logging.info("ConductorApp started (observer mode)")
        logging.info("No trading logic enabled")

        while True:
            self.heartbeat()
            time.sleep(self.interval)
