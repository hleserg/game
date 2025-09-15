#!/usr/bin/env python3
"""
Скрипт для запуска линтеров и проверки качества кода
"""

import subprocess
import sys
from pathlib import Path


def run_command(cmd: list[str], description: str) -> bool:
    """Запуск команды и возврат статуса успеха"""
    print(f"\n🔍 {description}")
    print(f"Команда: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("✅ Успешно!")
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print("❌ Ошибка!")
        if e.stdout:
            print("STDOUT:", e.stdout)
        if e.stderr:
            print("STDERR:", e.stderr)
        return False


def main():
    """Основная функция"""
    print("🚀 Запуск проверки качества кода")
    
    # Переходим в корневую директорию проекта
    project_root = Path(__file__).parent.parent
    print(f"📁 Рабочая директория: {project_root}")
    
    # Команды для проверки
    commands = [
        (["python", "-m", "ruff", "check", "src/"], "Ruff - проверка стиля кода"),
        (["python", "-m", "ruff", "format", "--check", "src/"], "Ruff - проверка форматирования"),
        (["python", "-m", "mypy", "src/", "--ignore-missing-imports"], "MyPy - проверка типов"),
        (["python", "-m", "pytest", "tests/", "-v", "--tb=short"], "Pytest - unit-тесты"),
    ]
    
    # Запускаем все команды
    success_count = 0
    for cmd, description in commands:
        if run_command(cmd, description):
            success_count += 1
    
    # Результат
    total_commands = len(commands)
    print(f"\n📊 Результат: {success_count}/{total_commands} проверок прошли успешно")
    
    if success_count == total_commands:
        print("🎉 Все проверки прошли успешно!")
        return 0
    else:
        print("⚠️  Некоторые проверки не прошли")
        return 1


if __name__ == "__main__":
    sys.exit(main())
