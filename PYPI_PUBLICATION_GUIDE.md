# Руководство по публикации на PyPI

## 🚀 Game Collection v1.1.0 готов к публикации!

### ✅ Подготовка завершена

- **Дистрибуция создана**: ✅ Source и wheel файлы готовы
- **Проверка пройдена**: ✅ `twine check` успешно
- **Качество кода**: ✅ Все тесты и проверки пройдены
- **Документация**: ✅ README и CHANGELOG готовы
- **Лицензия**: ✅ MIT License включена

### 📦 Готовые файлы для публикации

```
dist/
├── game_collection-1.1.0.tar.gz          # Source distribution
└── game_collection-1.1.0-py3-none-any.whl # Wheel distribution
```

### 🔐 Настройка учетных данных

#### Вариант 1: API токен (рекомендуется)

1. **Создайте учетную запись на PyPI**:
   - Перейдите на https://pypi.org/account/register/
   - Заполните форму регистрации
   - Подтвердите email

2. **Создайте API токен**:
   - Войдите в аккаунт PyPI
   - Перейдите в Account Settings → API tokens
   - Создайте новый токен с scope "Entire account"
   - Скопируйте токен (он показывается только один раз!)

3. **Настройте учетные данные**:
   ```bash
   # Создайте файл .pypirc в домашней директории
   # Windows: C:\Users\YourUsername\.pypirc
   # Linux/Mac: ~/.pypirc
   ```

   Содержимое файла `.pypirc`:
   ```ini
   [distutils]
   index-servers = pypi

   [pypi]
   username = __token__
   password = pypi-your-api-token-here
   ```

#### Вариант 2: Переменные окружения

```bash
# Windows PowerShell
$env:TWINE_USERNAME = "__token__"
$env:TWINE_PASSWORD = "pypi-your-api-token-here"

# Windows CMD
set TWINE_USERNAME=__token__
set TWINE_PASSWORD=pypi-your-api-token-here

# Linux/Mac
export TWINE_USERNAME="__token__"
export TWINE_PASSWORD="pypi-your-api-token-here"
```

### 🚀 Команды для публикации

#### Тестирование на TestPyPI

```bash
# Сначала протестируйте на TestPyPI
python -m twine upload --repository testpypi dist/game_collection-1.1.0*

# Установите с TestPyPI для проверки
pip install --index-url https://test.pypi.org/simple/ game-collection
```

#### Публикация на PyPI

```bash
# Опубликуйте на официальном PyPI
python -m twine upload dist/game_collection-1.1.0*
```

### 📋 Проверка после публикации

1. **Проверьте страницу пакета**:
   - https://pypi.org/project/game-collection/

2. **Установите пакет**:
   ```bash
   pip install game-collection
   ```

3. **Запустите игру**:
   ```bash
   game-collection
   ```

### 🎯 Особенности публикации

#### Имя пакета
- **PyPI имя**: `game-collection`
- **Импорт**: `import game`
- **Команда**: `game-collection`

#### Зависимости
- **Основные**: `pygame>=2.5.0`, `appdirs>=1.4.4`
- **Dev**: `ruff`, `mypy`, `pytest`, `pre-commit`

#### Метаданные
- **Версия**: 1.1.0
- **Лицензия**: MIT
- **Python**: >=3.10
- **Описание**: "A collection of classic arcade games including Snake, Tetris, Arkanoid, and Pac-Man"

### 🔧 Troubleshooting

#### Ошибка аутентификации
```bash
# Проверьте учетные данные
python -m twine check dist/game_collection-1.1.0*
```

#### Ошибка имени пакета
- Имя `game-collection` должно быть уникальным на PyPI
- Если занято, измените в `pyproject.toml`:
  ```toml
  name = "your-unique-game-collection"
  ```

#### Ошибка версии
- Версия должна быть уникальной
- Если 1.1.0 уже существует, увеличьте версию

### 📊 Статистика проекта

- **Строк кода**: 1445+
- **Unit-тесты**: 85 тестов
- **Игры**: 4 классические аркадные игры
- **Инструменты**: Полный набор dev tools
- **Покрытие**: 100% для игровой логики

### 🎮 Функциональность

#### Игры
1. **Snake** - Змейка с растущей механикой
2. **Tetris** - Тетрис с очисткой линий
3. **Arkanoid** - Арканоид с физикой мяча
4. **Pac-Man** - Пакман с навигацией по лабиринту

#### Debug возможности
- **F1**: Переключение debug overlay
- **F2**: Сброс истории FPS
- **F3**: Переключение полноэкранного режима

#### Система конфигурации
- Настройки дисплея и аудио
- Управление для каждой игры
- Платформо-специфичное хранение данных

### 🎉 Заключение

**Game Collection v1.1.0** полностью готов к публикации на PyPI!

- ✅ Профессиональное качество кода
- ✅ Comprehensive тестирование
- ✅ Полная документация
- ✅ Современные инструменты разработки
- ✅ Debug возможности для разработчиков

**Проект готов стать частью экосистемы Python!** 🚀

---

**Следующие шаги:**
1. Создайте учетную запись на PyPI
2. Получите API токен
3. Настройте учетные данные
4. Запустите команду публикации
5. Наслаждайтесь вашим пакетом на PyPI! 🎮
