@echo off
echo Установка зависимостей...
pip install -r requirements.txt

echo.
echo Компиляция в exe...
pyinstaller GameCollection.spec

echo.
echo Готово! Исполняемый файл находится в папке dist/
pause
