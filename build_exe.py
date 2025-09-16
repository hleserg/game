#!/usr/bin/env python3
"""Build script for GameCollection executable with proper assets."""

import os
import shutil
import subprocess
import sys
from pathlib import Path


def clean_build() -> None:
    """Clean previous build artifacts."""
    print("🧹 Cleaning previous build...")

    dirs_to_clean = ["build", "dist"]
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"   Removed {dir_name}/")

    # Clean .spec file if it exists
    spec_file = "GameCollection.spec"
    if os.path.exists(spec_file):
        print(f"   Keeping {spec_file}")


def check_assets() -> bool:
    """Check if required assets exist."""
    print("🔍 Checking assets...")

    required_assets = ["assets/icon.ico", "file_version.txt"]

    missing_assets = []
    for asset in required_assets:
        if not os.path.exists(asset):
            missing_assets.append(asset)
        else:
            print(f"   ✅ {asset}")

    if missing_assets:
        print("❌ Missing required assets:")
        for asset in missing_assets:
            print(f"   - {asset}")
        return False

    return True


def build_executable() -> bool:
    """Build the executable using PyInstaller."""
    print("🔨 Building executable...")

    # PyInstaller command
    cmd = ["pyinstaller", "--clean", "--noconfirm", "GameCollection.spec"]

    print(f"   Running: {' '.join(cmd)}")

    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("   ✅ Build successful!")
        return True
    except subprocess.CalledProcessError as e:
        print("   ❌ Build failed!")
        print(f"   Error: {e.stderr}")
        return False


def verify_build() -> bool:
    """Verify the built executable."""
    print("🔍 Verifying build...")

    exe_path = Path("dist/GameCollection.exe")
    if exe_path.exists():
        size_mb = exe_path.stat().st_size / (1024 * 1024)
        print(f"   ✅ Executable created: {exe_path}")
        print(f"   📦 Size: {size_mb:.1f} MB")
        return True
    else:
        print(f"   ❌ Executable not found: {exe_path}")
        return False


def create_release_package() -> None:
    """Create a release package."""
    print("📦 Creating release package...")

    release_dir = Path("release")
    release_dir.mkdir(exist_ok=True)

    # Copy executable
    exe_src = Path("dist/GameCollection.exe")
    exe_dst = release_dir / "GameCollection.exe"

    if exe_src.exists():
        shutil.copy2(exe_src, exe_dst)
        print(f"   ✅ Copied: {exe_dst}")

    # Create README for release
    readme_content = """# Game Collection v1.1.14

## 🎮 Установка и запуск

1. Скачайте `GameCollection.exe`
2. Запустите файл
3. Наслаждайтесь игрой!

## 🎯 Игры

- **🐍 Snake** - Классическая змейка
- **🧩 Tetris** - Тетрис с блоками
- **🎯 Arkanoid** - Арканоид с шариком
- **👻 Pac-Man** - Пакман в лабиринте

## ⚙️ Управление

- **Стрелки** - Движение
- **Пробел** - Пауза/Запуск
- **ESC** - Выход
- **F1** - Отладка (если включена)

## 📁 Данные

Игра сохраняет настройки и рекорды в:
- Windows: `%LOCALAPPDATA%\\hleserg\\GameCollection\\`
- macOS: `~/Library/Application Support/GameCollection/`
- Linux: `~/.local/share/GameCollection/`

---
*Собрано с помощью PyInstaller*
"""

    readme_path = release_dir / "README.md"
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)
    print(f"   ✅ Created: {readme_path}")


def main() -> None:
    """Main build process."""
    print("🚀 GameCollection Build Script")
    print("=" * 40)

    # Clean previous build
    clean_build()

    # Check assets
    if not check_assets():
        print("❌ Missing required assets. Please create them first.")
        sys.exit(1)

    # Build executable
    if not build_executable():
        print("❌ Build failed!")
        sys.exit(1)

    # Verify build
    if not verify_build():
        print("❌ Build verification failed!")
        sys.exit(1)

    # Create release package
    create_release_package()

    print("\n🎉 Build completed successfully!")
    print("📁 Executable: dist/GameCollection.exe")
    print("📦 Release: release/GameCollection.exe")


if __name__ == "__main__":
    main()
