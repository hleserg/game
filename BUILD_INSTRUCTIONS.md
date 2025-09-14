# Инструкция по компиляции в exe

## Быстрая компиляция

### Способ 1: Использование bat файла
Просто запустите файл `build.bat` - он автоматически установит зависимости и скомпилирует игру.

### Способ 2: Ручная компиляция

1. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Скомпилируйте игру:**
   ```bash
   pyinstaller GameCollection.spec
   ```

3. **Найдите исполняемый файл:**
   Готовый exe файл будет в папке `dist/GameCollection.exe`

## Дополнительные опции компиляции

### Создание архива
```bash
pyinstaller --onefile --windowed --name "GameCollection" main.py
```

### Компиляция с консолью (для отладки)
```bash
pyinstaller --onefile --console --name "GameCollection" main.py
```

### Компиляция с иконкой
```bash
pyinstaller --onefile --windowed --icon=icon.ico --name "GameCollection" main.py
```

## Размер файла

После компиляции размер exe файла составит примерно 15-20 МБ.

## Требования для запуска

Скомпилированный exe файл не требует установки Python или pygame - все зависимости включены.

## Устранение проблем

### Ошибка "pygame not found"
Убедитесь, что pygame установлен:
```bash
pip install pygame
```

### Ошибка "PyInstaller not found"
Установите PyInstaller:
```bash
pip install pyinstaller
```

### Большой размер файла
Используйте флаг `--exclude-module` для исключения ненужных модулей:
```bash
pyinstaller --onefile --windowed --exclude-module tkinter --name "GameCollection" main.py
```
