"""
Модуль для підрахунку загальної та середньої заробітної плати з текстового файлу.
Файл має містити рядки у форматі: ім'я,зарплата (одна пара на рядок).
"""

from os.path import exists


def total_salary(path: str) -> tuple[int, float]:
    """
    Обчислює загальну та середню заробітну плату з файлу.

    Args:
        path: Шлях до текстового файлу (UTF-8, рядки: "ім'я,число").

    Returns:
        Кортеж (total, average): загальна сума та середня зарплата.

    Raises:
        FileNotFoundError: Якщо файл не існує або не відкривається.
        Exception: При помилці читання або парсингу.
    """
    if not exists(path):
        raise FileNotFoundError(f"File '{path}' does not exist.")

    total = 0
    count = 0

    try:
        with open(path, encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                _, salary = line.split(",")
                total += int(salary)
                count += 1

            if count == 0:
                return 0, 0.0

    except ValueError as ex:
        raise ValueError(f"Invalid file format: {ex}") from ex
    except Exception as ex:
        raise RuntimeError(f"Something went wrong: {ex}") from ex

    return total, total / count


if __name__ == "__main__":
    total, average = total_salary("task1.txt")
    print(
        f"Загальна сума заробітної плати: {total}, "
        f"Середня заробітна плата: {average:.2f}"
    )
