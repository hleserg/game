@echo off
echo ========================================
echo    Game Collection - Установка
echo ========================================
echo.

echo Проверка Python...
python --version
if %errorlevel% neq 0 (
    echo ОШИБКА: Python не найден!
    pause
    exit /b 1
)

echo.
echo Проверка pygame...
python -c "import pygame; print('pygame OK')" 2>nul
if %errorlevel% neq 0 (
    echo pygame не найден, попытка установки...
    pip install pygame --user
)

echo.
echo Установка Game Collection...
pip install game-collection --no-deps --user

echo.
echo Проверка установки...
python -c "import game; print('Game Collection установлен!')"

echo.
echo ========================================
echo    Установка завершена!
echo ========================================
echo.
echo Способы запуска:
echo   1. python -m game
echo   2. python main.py
echo   3. game-collection (если PATH настроен)
echo.
echo Для настройки команды game-collection запустите:
echo   setup_path.bat
echo.
pause
