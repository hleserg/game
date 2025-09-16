# Инструкция по созданию релиза v1.1.11

## 📦 Готовые файлы для релиза:

1. **GameCollection-v1.1.11-Windows-Fixed.zip** (14.9 МБ) ⭐ **РЕКОМЕНДУЕТСЯ**
   - Исправленный исполняемый файл для Windows
   - Включены шрифты pygame
   - README с инструкциями
   - Готов к распространению

2. **GameCollection-v1.1.11-Source.zip** (41.1 МБ)
   - Исходный код проекта
   - Полная история git
   - Для разработчиков

## 🚀 Как создать релиз на GitHub:

1. **Перейдите на страницу релизов:**
   https://github.com/hleserg/game/releases

2. **Нажмите "Create a new release"**

3. **Выберите тег:** `v1.1.11`

4. **Заголовок релиза:**
   ```
   Game Collection v1.1.11 - Исправления интерфейса игр
   ```

5. **Описание релиза:**
   ```markdown
   ## 🎮 Game Collection v1.1.11

   ### Основные изменения:
   - ✅ Исправлено наложение элементов интерфейса в Тетрисе
   - ✅ Перемещена секция 'Следующая' ниже управления в Тетрисе
   - ✅ Исправлено отображение символов стрелок в Арканоиде
   - ✅ Уменьшен размер шрифта инструкций в Арканоиде
   - ✅ Перемещен текст статистики выше кирпичей в Арканоиде
   - ✅ Смещены инструкции влево в главном меню

   ### 🎮 Игры:
   - **🐍 Snake** - Classic snake game with growing mechanics
   - **🎯 Arkanoid** - Breakout-style game with paddle and ball physics
   - **🧩 Tetris** - Block-stacking puzzle game with line clearing
   - **👻 Pac-Man** - Maze navigation game with dots and ghosts

   ### 🔧 Технические улучшения:
   - Улучшено расположение элементов UI
   - Исправлены проблемы с отображением символов
   - Оптимизированы размеры шрифтов
   - Улучшена читаемость интерфейса
   - Добавлена безопасность API токенов

   ### 📦 Файлы релиза:
   - **Windows**: `GameCollection-v1.1.11-Windows-Fixed.zip` - готовый к запуску исполняемый файл (исправлены шрифты)
   - **Source**: `GameCollection-v1.1.11-Source.zip` - исходный код для разработчиков

   ### 🚀 Установка:
   1. Скачайте `GameCollection-v1.1.11-Windows-Fixed.zip`
   2. Распакуйте архив
   3. Запустите `GameCollection.exe`
   4. Наслаждайтесь игрой!

   ---
   *Собрано с помощью PyInstaller для Windows*
   ```

6. **Загрузите файлы:**
   - Перетащите `GameCollection-v1.1.11-Windows-Fixed.zip` в область "Attach binaries"
   - Перетащите `GameCollection-v1.1.11-Source.zip` в область "Attach binaries"

7. **Нажмите "Publish release"**

## ✅ Результат:
После публикации релиз будет доступен по адресу:
https://github.com/hleserg/game/releases/tag/v1.1.11

Пользователи смогут скачать готовый исполняемый файл и играть без установки Python!
