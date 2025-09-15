#!/usr/bin/env python3
"""
Скрипт для форматирования кода с помощью Ruff
"""

import subprocess
import sys
from pathlib import Path


def run_ruff_format() -> bool:
    """Запуск Ruff formatter"""
    try:
        result = subprocess.run(
            ["ruff", "format", "."],
            capture_output=True,
            text=True,
            cwd=Path(__file__).parent.parent,
        )

        if result.stdout:
            print("Форматирование выполнено:")
            print(result.stdout)

        if result.stderr:
            print("Предупреждения:")
            print(result.stderr)

        return result.returncode == 0

    except FileNotFoundError:
        print("❌ Ruff не найден. Установите его: pip install ruff")
        return False


def run_ruff_check() -> bool:
    """Запуск Ruff linter"""
    try:
        result = subprocess.run(
            ["ruff", "check", "."], capture_output=True, text=True, cwd=Path(__file__).parent.parent
        )

        if result.stdout:
            print("Найдены проблемы:")
            print(result.stdout)
            return False

        print("✅ Код соответствует стандартам!")
        return True

    except FileNotFoundError:
        print("❌ Ruff не найден. Установите его: pip install ruff")
        return False


def main() -> None:
    """Основная функция"""
    print("🔧 Запуск форматирования кода...")

    # Форматирование
    if not run_ruff_format():
        print("❌ Ошибка форматирования")
        sys.exit(1)

    # Проверка
    if not run_ruff_check():
        print("❌ Код не прошел проверку")
        sys.exit(1)

    print("✅ Все проверки пройдены!")


if __name__ == "__main__":
    main()
