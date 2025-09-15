# 🪟 Руководство по установке Game Collection в Windows

## ❌ **Проблема: Ошибка прав доступа при установке pygame**

### Симптомы:
```
ERROR: Could not install packages due to an OSError: [WinError 5] Отказано в доступе: 'C:\\Users\\Serg\\AppData\\Roaming\\Python\\Python313\\site-packages\\pygame\\SDL2.dll'
Check the permissions.
```

### Причина:
Windows блокирует обновление файлов pygame, которые могут быть заблокированы другими процессами или антивирусом.

---

## ✅ **РЕШЕНИЯ (выберите подходящее):**

### **Решение 1: Установка без зависимостей (РЕКОМЕНДУЕТСЯ)**
```bash
pip install game-collection --no-deps --user
```
**Плюсы**: Быстро, безопасно, работает с уже установленным pygame
**Минусы**: Нет

### **Решение 2: Установка в виртуальное окружение**
```bash
# Создание виртуального окружения
python -m venv game_env

# Активация (Windows)
game_env\Scripts\activate

# Установка
pip install game-collection

# Запуск
python -m game
```

### **Решение 3: Установка от имени администратора**
1. Откройте PowerShell от имени администратора
2. Выполните: `pip install game-collection`

### **Решение 4: Принудительная переустановка pygame**
```bash
pip uninstall pygame -y
pip install pygame --user
pip install game-collection --user
```

---

## 🎮 **Проверка установки:**

### 1. Проверка pygame:
```bash
python -c "import pygame; print(f'pygame версия: {pygame.version.ver}')"
```

### 2. Проверка game-collection:
```bash
pip show game-collection
```

### 3. Запуск игры:
```bash
# Через модуль (всегда работает)
python -m game

# Через локальный файл
python main.py

# Через команду (если PATH настроен)
game-collection
```

---

## 🔧 **Настройка команды game-collection:**

### Если команда не найдена:
```bash
game-collection: The term 'game-collection' is not recognized
```

### Решение:
1. **Временное (для текущей сессии):**
   ```powershell
   $env:PATH += ";C:\Users\Serg\AppData\Roaming\Python\Python313\Scripts"
   game-collection
   ```

2. **Постоянное:**
   - Запустите `setup_path.bat` от имени администратора
   - Перезапустите терминал
   - Используйте `game-collection`

---

## ⚠️ **Предупреждения (можно игнорировать):**

### 1. Предупреждение о pygame.threads:
```
RuntimeWarning: import threads: No module named 'pygame.threads'
```
**Статус**: ✅ Не критично, игра работает нормально

### 2. Предупреждение о недействительной дистрибуции:
```
WARNING: Ignoring invalid distribution ~ygame
```
**Статус**: ✅ Не критично, pygame работает

---

## 🚀 **Быстрый старт для Windows:**

### Шаг 1: Установка
```bash
pip install game-collection --no-deps --user
```

### Шаг 2: Проверка
```bash
python -c "import pygame; print('pygame OK')"
python -m game
```

### Шаг 3: Настройка команды (опционально)
```bash
setup_path.bat
```

### Шаг 4: Запуск
```bash
game-collection
# или
python -m game
```

---

## 📋 **Альтернативные способы запуска:**

### 1. Через модуль (рекомендуется):
```bash
python -m game
```

### 2. Через локальный файл:
```bash
python main.py
```

### 3. Через entry-point (если PATH настроен):
```bash
game-collection
```

---

## 🔍 **Диагностика проблем:**

### Проверка Python:
```bash
python --version
```

### Проверка pip:
```bash
pip --version
```

### Проверка pygame:
```bash
python -c "import pygame; print(pygame.version.ver)"
```

### Проверка game-collection:
```bash
pip show game-collection
```

### Проверка PATH:
```bash
echo $env:PATH
```

---

## 💡 **Советы:**

1. **Всегда используйте `--user`** для установки в пользовательскую директорию
2. **Используйте `--no-deps`** если есть проблемы с зависимостями
3. **Запускайте через `python -m game`** если команда не работает
4. **Игнорируйте предупреждения** о pygame.threads - они не критичны

---

## 🎯 **Итог:**

**Game Collection работает в Windows!** Даже если есть проблемы с установкой pygame, игра запускается через:
- `python -m game`
- `python main.py`

**Главное**: pygame уже установлен и работает, поэтому игра функционирует нормально!
