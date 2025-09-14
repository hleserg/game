import json
import os
from datetime import datetime

class ScoreManager:
    def __init__(self):
        self.scores_file = "scores.json"
        self.scores = self.load_scores()
    
    def load_scores(self):
        """Загрузка рекордов из файла"""
        if os.path.exists(self.scores_file):
            try:
                with open(self.scores_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return {}
        return {}
    
    def save_scores(self):
        """Сохранение рекордов в файл"""
        try:
            with open(self.scores_file, 'w', encoding='utf-8') as f:
                json.dump(self.scores, f, ensure_ascii=False, indent=2)
        except IOError:
            pass  # Игнорируем ошибки записи
    
    def add_score(self, game_name, score):
        """Добавление нового рекорда"""
        if game_name not in self.scores:
            self.scores[game_name] = []
        
        # Создаем запись о рекорде
        score_entry = {
            "player": "Игрок",  # Можно расширить для ввода имени
            "score": score,
            "date": datetime.now().strftime("%d.%m.%Y %H:%M")
        }
        
        # Добавляем рекорд
        self.scores[game_name].append(score_entry)
        
        # Сортируем по убыванию очков
        self.scores[game_name].sort(key=lambda x: x['score'], reverse=True)
        
        # Оставляем только топ 10
        self.scores[game_name] = self.scores[game_name][:10]
        
        # Сохраняем
        self.save_scores()
    
    def get_scores(self, game_name):
        """Получение рекордов для конкретной игры"""
        return self.scores.get(game_name, [])
    
    def get_best_score(self, game_name):
        """Получение лучшего рекорда для игры"""
        scores = self.get_scores(game_name)
        if scores:
            return scores[0]['score']
        return 0
    
    def clear_scores(self, game_name=None):
        """Очистка рекордов"""
        if game_name:
            if game_name in self.scores:
                del self.scores[game_name]
        else:
            self.scores = {}
        self.save_scores()
