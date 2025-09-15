#!/usr/bin/env python3
"""Скрипт для публикации Game Collection на PyPI."""

import subprocess
import sys
from pathlib import Path


def run_command(cmd: list[str], description: str) -> bool:
    """Запустить команду и показать результат."""
    print(f"🔧 {description}")
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


def main() -> int:
    """Основная функция публикации."""
    print("🚀 Публикация Game Collection на PyPI")
    print("=" * 50)

    # Переходим в корневую директорию проекта
    project_root = Path(__file__).parent.parent
    print(f"📁 Рабочая директория: {project_root}")

    # Проверяем наличие дистрибуции
    dist_dir = project_root / "dist"
    if not dist_dir.exists():
        print("❌ Директория dist/ не найдена!")
        print("Сначала создайте дистрибуцию: python -m build")
        return 1

    # Проверяем файлы дистрибуции
    dist_files = list(dist_dir.glob("game_collection-1.1.0*"))
    if not dist_files:
        print("❌ Файлы дистрибуции game_collection-1.1.0* не найдены!")
        print("Сначала создайте дистрибуцию: python -m build")
        return 1

    print(f"📦 Найдены файлы дистрибуции: {len(dist_files)}")
    for file in dist_files:
        print(f"  - {file.name}")

    # Проверяем дистрибуцию
    if not run_command(
        ["python", "-m", "twine", "check", "dist/game_collection-1.1.0*"], "Проверка дистрибуции"
    ):
        return 1

    print("\n" + "=" * 50)
    print("🎯 Готово к публикации!")
    print("\nДля публикации выполните одну из команд:")
    print("\n1. Тестирование на TestPyPI:")
    print("   python -m twine upload --repository testpypi dist/game_collection-1.1.0*")
    print("\n2. Публикация на PyPI:")
    print("   python -m twine upload dist/game_collection-1.1.0*")
    print("\n📋 Не забудьте:")
    print("   - Создать учетную запись на PyPI")
    print("   - Получить API токен")
    print("   - Настроить учетные данные в .pypirc")
    print("\n📖 Подробная инструкция: PYPI_PUBLICATION_GUIDE.md")

    return 0


if __name__ == "__main__":
    sys.exit(main())
