# 🔧 Решение проблем с Game Collection

## ❌ **Проблема 1: Ошибка прав доступа при установке pygame**

### Симптомы:
```
ERROR: Could not install packages due to an OSError: [WinError 5] Отказано в доступе: 'C:\\Users\\Serg\\AppData\\Roaming\\Python\\Python313\\site-packages\\pygame\\SDL2.dll'
```

### Решение:
```bash
# Установка только нашего пакета без обновления pygame
pip install game-collection --no-deps --user
```

**Объяснение**: pygame заблокирован системой, но наш пакет может работать с уже установленной версией pygame.

---

## ❌ **Проблема 2: Команда game-collection не найдена**

### Симптомы:
```
game-collection: The term 'game-collection' is not recognized as a name of a cmdlet, function, script file, or executable program.
```

### Решение:

#### Вариант 1: Временное решение (для текущей сессии)
```powershell
$env:PATH += ";C:\Users\Serg\AppData\Roaming\Python\Python313\Scripts"
game-collection
```

#### Вариант 2: Постоянное решение
1. Запустите `setup_path.bat` от имени администратора
2. Перезапустите терминал
3. Используйте команду `game-collection`

#### Вариант 3: Альтернативный запуск
```bash
# Через модуль (всегда работает)
python -m game

# Через локальный файл
python main.py
```

---

## ❌ **Проблема 3: Предупреждение о pygame.threads**

### Симптомы:
```
RuntimeWarning: import threads: No module named 'pygame.threads'
```

### Решение:
**Это не критично!** Игра работает нормально. Это предупреждение можно игнорировать.

---

## ✅ **Проверка работоспособности**

### 1. Проверка установки:
```bash
pip show game-collection
```

### 2. Проверка команды:
```bash
game-collection
```

### 3. Проверка модуля:
```bash
python -m game
```

### 4. Проверка локального запуска:
```bash
python main.py
```

---

## 🎮 **Управление в игре**

### Основные клавиши:
- **Стрелки** - Движение в играх
- **Пробел** - Действие/пауза
- **Enter** - Подтверждение
- **Escape** - Выход/назад

### Отладочные клавиши:
- **F1** - Переключение debug overlay
- **F2** - Сброс истории FPS
- **F3** - Переключение полноэкранного режима

---

## 📋 **Часто задаваемые вопросы**

### Q: Почему не работает установка pygame?
A: Это проблема прав доступа Windows. Используйте `--no-deps` для установки только нашего пакета.

### Q: Почему команда game-collection не найдена?
A: Путь к Python Scripts не добавлен в PATH. Используйте `setup_path.bat` или запускайте через `python -m game`.

### Q: Можно ли играть без установки пакета?
A: Да! Запускайте через `python main.py` или `python -m game`.

### Q: Что делать, если игра не запускается?
A: Проверьте, что pygame установлен: `pip show pygame`

---

## 🚀 **Быстрый старт**

### Для разработчиков:
```bash
# Клонирование и установка
git clone <repository>
cd game
pip install -e .[dev]

# Запуск
python -m game
```

### Для пользователей:
```bash
# Установка
pip install game-collection --no-deps --user

# Настройка PATH (один раз)
setup_path.bat

# Запуск
game-collection
```

---

## 📞 **Поддержка**

Если проблемы остаются:
1. Проверьте версию Python: `python --version`
2. Проверьте версию pygame: `pip show pygame`
3. Проверьте версию game-collection: `pip show game-collection`
4. Попробуйте запуск через модуль: `python -m game`

**Помните**: Игра всегда работает через `python -m game` или `python main.py`!
