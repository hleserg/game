# 🎨 Руководство по работе с ассетами

## 📁 Структура ассетов

```
assets/
├── icon.ico              # Иконка приложения
├── fonts/                # Шрифты
│   └── freesansbold.ttf
├── sounds/               # Звуковые эффекты
│   ├── game_start.wav
│   ├── game_over.wav
│   └── score.wav
└── images/              # Изображения
    ├── background.png
    ├── sprites/
    │   ├── snake_head.png
    │   ├── tetris_block.png
    │   └── pacman.png
    └── ui/
        ├── button.png
        └── menu_bg.png
```

## 🔧 Настройка PyInstaller

### GameCollection.spec
```python
# Добавление ассетов в сборку
datas=[
    ('src/game/config.json', 'game'),
    ('src/game/games', 'game/games'),
    ('src/game/ui', 'game/ui'),
    ('assets', 'assets'),                    # Все ассеты
    ('file_version.txt', '.'),              # Метаданные версии
    (pygame_fonts_path, 'pygame')
],

# Настройка исполняемого файла
exe = EXE(
    # ... другие параметры ...
    icon='assets/icon.ico',                 # Иконка приложения
    version='file_version.txt',             # Метаданные версии
)
```

### file_version.txt
```python
VSVersionInfo(
  ffi=FixedFileInfo(
    filevers=(1,1,14,0),                   # Версия файла
    prodvers=(1,1,14,0),                   # Версия продукта
    # ... другие параметры ...
  ),
  kids=[
    StringFileInfo([
      StringTable(u'040904B0', [
        StringStruct(u'CompanyName', u'hleserg'),
        StringStruct(u'FileDescription', u'Game Collection - Classic Arcade Games'),
        StringStruct(u'FileVersion', u'1.1.14'),
        StringStruct(u'ProductName', u'Game Collection'),
        # ... другие метаданные ...
      ])
    ])
  ]
)
```

## 🐍 Использование в коде

### Импорт утилит
```python
from game.assets import (
    get_asset_path,
    get_icon_path,
    get_font_path,
    get_sound_path,
    get_image_path,
    asset_exists
)
```

### Получение путей к ассетам
```python
# Иконка приложения
icon_path = get_icon_path()

# Шрифт
font_path = get_font_path("freesansbold.ttf")

# Звук
sound_path = get_sound_path("game_start.wav")

# Изображение
image_path = get_image_path("background.png")

# Произвольный ассет
custom_path = get_asset_path("custom/file.txt")
```

### Проверка существования
```python
if asset_exists("sounds/game_start.wav"):
    # Загрузить звук
    sound = pygame.mixer.Sound(get_sound_path("game_start.wav"))
else:
    # Использовать заглушку
    print("Sound file not found")
```

### Загрузка ресурсов
```python
import pygame
from game.assets import get_image_path, get_font_path

# Загрузка изображения
def load_image(image_name):
    image_path = get_image_path(image_name)
    if image_path.exists():
        return pygame.image.load(str(image_path))
    else:
        # Создать заглушку
        return pygame.Surface((32, 32))

# Загрузка шрифта
def load_font(font_name, size):
    font_path = get_font_path(font_name)
    if font_path.exists():
        return pygame.font.Font(str(font_path), size)
    else:
        # Использовать системный шрифт
        return pygame.font.Font(None, size)
```

## 🚀 Сборка с ассетами

### Автоматическая сборка
```bash
# Использовать скрипт сборки
python build_exe.py
```

### Ручная сборка
```bash
# Очистка
pyinstaller --clean GameCollection.spec

# Сборка
pyinstaller GameCollection.spec
```

### CLI параметры
```bash
# С иконкой
pyinstaller --icon assets/icon.ico src/game/__main__.py

# С ассетами
pyinstaller --add-data "assets;assets" src/game/__main__.py

# Полная команда
pyinstaller \
  --onefile \
  --windowed \
  --icon assets/icon.ico \
  --add-data "assets;assets" \
  --add-data "src/game/config.json;game" \
  --name GameCollection \
  src/game/__main__.py
```

## 🔍 Отладка ассетов

### Проверка путей
```python
# Тестирование утилиты ассетов
python src/game/assets.py
```

### Проверка в собранном приложении
```python
import sys
print(f"MEIPASS: {getattr(sys, '_MEIPASS', 'Not in PyInstaller')}")

# Проверить все ассеты
from game.assets import list_assets
assets = list_assets()
for asset in assets:
    print(f"Asset: {asset}")
```

## 📋 Рекомендации

### ✅ Лучшие практики:
1. **Всегда проверяйте существование** ассетов перед загрузкой
2. **Используйте утилиты** из `game.assets` для получения путей
3. **Добавляйте ассеты в .spec** файл для включения в сборку
4. **Тестируйте сборку** после добавления новых ассетов
5. **Используйте относительные пути** в коде

### ❌ Избегайте:
1. **Хардкода абсолютных путей** в коде
2. **Прямого обращения к sys._MEIPASS** (используйте утилиты)
3. **Забывания добавить ассеты** в .spec файл
4. **Игнорирования ошибок** загрузки ассетов

## 🎯 Примеры использования

### В игре Snake
```python
from game.assets import get_image_path

class SnakeGame:
    def __init__(self):
        # Загрузка спрайтов
        self.head_sprite = self.load_image("sprites/snake_head.png")
        self.body_sprite = self.load_image("sprites/snake_body.png")
        self.food_sprite = self.load_image("sprites/food.png")

    def load_image(self, image_name):
        image_path = get_image_path(image_name)
        if image_path.exists():
            return pygame.image.load(str(image_path))
        else:
            # Создать простой спрайт
            surface = pygame.Surface((20, 20))
            surface.fill((255, 255, 255))
            return surface
```

### В меню
```python
from game.assets import get_image_path, get_sound_path

class Menu:
    def __init__(self):
        # Фон меню
        bg_path = get_image_path("ui/menu_bg.png")
        if bg_path.exists():
            self.background = pygame.image.load(str(bg_path))

        # Звук при наведении
        hover_sound_path = get_sound_path("ui/hover.wav")
        if hover_sound_path.exists():
            self.hover_sound = pygame.mixer.Sound(str(hover_sound_path))
```

---
*Руководство создано: 16.09.2025*
