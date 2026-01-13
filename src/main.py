"""
Conductor Server — entrypoint
Stage: observer / no trading
Purpose:
- load CONFIG.yml
- confirm server boot
- prepare architecture for data → decision → execution
"""

import sys
from pathlib import Path
import yaml
from datetime import datetime


ROOT_DIR = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT_DIR / "CONFIG.yml"


def load_config(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"CONFIG not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main():
    print("=" * 50)
    print("CONDUCTOR SERVER — BOOT")
    print(f"Time: {datetime.utcnow().isoformat()} UTC")

    try:
        config = load_config(CONFIG_PATH)
    except Exception as e:
        print("❌ CONFIG LOAD FAILED")
        print(e)
        sys.exit(1)

    print("✅ CONFIG LOADED")

    project = config.get("project", {})
    universe = config.get("universe", {})

    print(f"Project: {project.get('name')}")
    print(f"Exchange: {project.get('exchange')}")
    print(f"Mode: {project.get('mode')}")
    print(f"Timezone: {project.get('timezone')}")

    symbols = universe.get("symbols_watchlist", [])
    print(f"Symbols loaded: {len(symbols)}")
    for s in symbols:
        print(f" - {s}")

    print("=" * 50)
    print("STATUS: OBSERVER READY")
    print("Trading: DISABLED")
    print("Next step: market data layer")
    print("=" * 50)


if __name__ == "__main__":
    main()
