from Pong.pong_game import PongGame
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window


class MenuScreen(MDScreen):
    def switch_to_settings(self):
        self.manager.current = 'settings'


class SettingsScreen(MDScreen):
    def back_to_menu(self):
        self.manager.current = 'menu'


class PongGameScreen(MDScreen):
    def __init__(self, **kwargs):
        super(PongGameScreen, self).__init__(**kwargs)
        self.game = PongGame()
        Clock.schedule_interval(self.game.update, 1.0 / 60.0)
        self.add_widget(self.game)


class GameApp(MDApp):
    def __init__(self):
        super().__init__()
        self.orientation = 'landscape'

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.material_style = "M3"

        Builder.load_file('../CemsGameApp/Pong/pong_game.kv')
        Builder.load_file('../CemsGameApp/BlackJack/blackjack_game.kv')
        Builder.load_file('menu.kv')
        Builder.load_file('settings.kv')

        sm = MDScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(PongGameScreen(name='pong game'))
        return sm

    def on_start(self):
        # Window.fullscreen = 'auto'
        Window.size = (1800, 900)


if __name__ == '__main__':
    GameApp().run()
