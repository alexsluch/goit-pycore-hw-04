"""
Скрипт візуалізації структури директорії з кольоровим виводом (colorama).
Запуск: python task3.py <шлях_до_директорії>
"""

import sys
from pathlib import Path

from colorama import Fore, Style, init

init(autoreset=True)


def _tree(path: Path, prefix: str = "") -> None:
    if not path.is_dir():
        return
    entries = sorted(path.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower()))
    for i, entry in enumerate(entries):
        is_last = i == len(entries) - 1
        connector = "┗ " if is_last else "┣ "
        if entry.is_dir():
            print(f"{prefix}{connector}{Fore.BLUE}📂 {entry.name}{Style.RESET_ALL}")
            new_prefix = prefix + ("   " if is_last else "┃ ")
            _tree(entry, new_prefix)
        else:
            print(f"{prefix}{connector}{Fore.GREEN}📜 {entry.name}{Style.RESET_ALL}")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python task3.py <path_to_directory>", file=sys.stderr)
        sys.exit(1)

    dir_path = Path(sys.argv[1]).resolve()
    if not dir_path.exists():
        print(f"Error: path does not exist: {dir_path}", file=sys.stderr)
        sys.exit(1)
    if not dir_path.is_dir():
        print(f"Error: not a directory: {dir_path}", file=sys.stderr)
        sys.exit(1)

    print(f"{Fore.CYAN}📦 {dir_path.name}{Style.RESET_ALL}")
    _tree(dir_path)


if __name__ == "__main__":
    main()
