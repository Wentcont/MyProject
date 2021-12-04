class Settings:
    def __init__(self):
        # Параметры экрана
        self.screen_width = 1366
        self.screen_height = 768
        self.bg_color = (230, 230, 230)

        # Лимит кораблей
        self.ship_limit = 2

        # Параметры снаряда
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Настройки пришельцев
        self.fleet_drop_speed = 10

        # скорость игры
        self.speedup_scale = 1.1
        # скорость пришельцев
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.3

        # счет за 1 пришельца
        self.alien_points = 50

        # движение влево вправо
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
