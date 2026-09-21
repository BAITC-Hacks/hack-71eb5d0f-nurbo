#!/usr/bin/env python3
"""Фильтр шума: печатает только critical-события и summary «критичных N».

Без внешних зависимостей. Запуск: python3 filter_events.py [путь_к_файлу]
"""
import json
import sys
from pathlib import Path


def main() -> None:
    path = Path(sys.argv[1] if len(sys.argv) > 1 else "events.json")
    events = json.loads(path.read_text(encoding="utf-8"))

    critical = [e for e in events if e["level"] == "critical"]

    for e in critical:
        print(f"[{e['level']}] {e['event']}")
    print(f"критичных {len(critical)}")


if __name__ == "__main__":
    main()
