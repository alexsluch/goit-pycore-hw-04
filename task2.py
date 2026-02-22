"""
Модуль для читання інформації про котів з текстового файлу.
Формат рядка: id,ім'я,вік
"""

from pathlib import Path


def get_cats_info(path: str) -> list[dict[str, str]]:
    """
    Читає файл з даними про котів і повертає список словників.

    Args:
        path: Шлях до текстового файлу (UTF-8).

    Returns:
        Список словників з ключами "id", "name", "age".

    Raises:
        FileNotFoundError: Якщо файл не існує.
        PermissionError: Якщо немає доступу до файлу.
    """
    path_obj = Path(path)
    if not path_obj.exists():
        raise FileNotFoundError(f"File '{path}' does not exist.")
    if not path_obj.is_file():
        raise ValueError(f"'{path}' is not a file.")

    result = []
    with open(path, encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) != 3:
                raise ValueError(f"Invalid line format: {line!r}")
            cat_id, name, age = parts
            result.append({
                "id": cat_id.strip(),
                "name": name.strip(),
                "age": age.strip(),
            })
    return result


if __name__ == "__main__":
    cats_info = get_cats_info("task2.txt")
    print(cats_info)
