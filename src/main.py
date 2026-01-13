"""
Conductor Server — entrypoint
Stage: observer / no trading

Purpose:
- load CONFIG.yml
- confirm server boot
- init logging
- prepare directories
- run ConductorApp core loop
"""

from __future__ import annotations

import sys
import logging
from pathlib import Path
from datetime import datetime

import yaml

from app import ConductorApp


# project root: /conductor-core
ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "CONFIG.yml"


def setup_logging(log_dir: Path) -> None:
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "conductor.log"

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(log_file, encoding="utf-8"),
        ],
    )


def load_config(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(
            f"CONFIG.yml not found at {path}\n"
            f"Create CONFIG.yml in project root."
        )

    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("CONFIG.yml must contain key-value mapping")

    return data


def boot_banner(cfg: dict) -> None:
    stage = cfg.get("stage", "observer")
    run_id = datetime.utcnow().strftime("%Y%m%d-%H%M%S")

    logging.info("===================================")
    logging.info(" Conductor Server BOOT ✓")
    logging.info(" stage   : %s", stage)
    logging.info(" run_id  : %s", run_id)
    logging.info(" config  : %s", CONFIG_PATH)
    logging.info("===================================")


def prepare_dirs(cfg: dict) -> None:
    data_dir = ROOT / cfg.get("data_dir", "data")
    logs_dir = ROOT / cfg.get("logs_dir", "logs")

    data_dir.mkdir(parents=True, exist_ok=True)
    logs_dir.mkdir(parents=True, exist_ok=True)

    logging.info("Directories ready")
    logging.info(" data : %s", data_dir)
    logging.info(" logs : %s", logs_dir)


def main() -> int:
    cfg = load_config(CONFIG_PATH)

    logs_dir = ROOT / cfg.get("logs_dir", "logs")
    setup_logging(logs_dir)

    boot_banner(cfg)
    prepare_dirs(cfg)

    # connect boot -> app core
    app = ConductorApp(cfg)
    app.run()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
