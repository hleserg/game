# 🚀 GitHub Actions для коллекции игр

Этот репозиторий использует GitHub Actions для автоматической сборки и выкладки релизов.

## 📋 Workflows

### 🎯 Release (`.github/workflows/release.yml`)
- **Триггер**: Пуш тега `v*` (например, `v1.0.0`)
- **Платформы**: Windows и Linux
- **Результат**: Автоматическое создание релиза с исполняемыми файлами

### 🔨 Build PR (`.github/workflows/build.yml`)
- **Триггер**: Pull Request и пуш в main/master
- **Платформы**: Windows и Linux
- **Результат**: Артефакты для тестирования (хранятся 7 дней)

## 🎮 Как создать релиз

1. **Создайте тег**:
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```

2. **GitHub Actions автоматически**:
   - Соберет exe для Windows
   - Соберет исполняемый файл для Linux
   - Создаст релиз с обоими файлами
   - Добавит описание релиза

## 📦 Результаты сборки

### Windows
- **Файл**: `GameCollection.exe`
- **Размер**: ~18 МБ
- **Запуск**: Двойной клик

### Linux
- **Файл**: `GameCollection`
- **Размер**: ~18 МБ
- **Запуск**: `chmod +x GameCollection && ./GameCollection`

## 🧪 Тестирование

Workflow `build.yml` также включает тесты:
- Проверка импорта всех модулей
- Проверка версии pygame
- Проверка корректности игр

## 🔧 Настройка

Для работы workflows требуется:
- Python 3.11
- pygame >= 2.5.0
- pyinstaller >= 5.13.0

Все зависимости указаны в `requirements.txt`.
