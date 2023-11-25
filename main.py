from Pong.pong_game import PongGame
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.screenmanager import FadeTransition


class SplashScreen(MDScreen):
    pass


class LoginScreen(MDScreen):
    pass


class MenuScreen(MDScreen):
    def switch_to_settings(self):
        self.manager.current = 'settings'

    def switch_to_login_screen(self):
        self.manager.current = 'login'


class SettingsScreen(MDScreen):
    def back_to_menu(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'menu'


class PongGameScreen(MDScreen):
    def __init__(self, **kwargs):
        super(PongGameScreen, self).__init__(**kwargs)
        self.game = PongGame()
        self.add_widget(self.game)


class GameApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.accent_palette = "LightGreen"
        self.theme_cls.accent_hue = "900"
        self.theme_cls.material_style = "M3"

        Builder.load_file('../CemsGameApp/Pong/pong_game.kv')
        Builder.load_file('../CemsGameApp/BlackJack/blackjack_game.kv')
        Builder.load_file('splashScreen.kv')
        Builder.load_file('login.kv')
        Builder.load_file('menu.kv')
        Builder.load_file('settings.kv')

        sm = MDScreenManager()
        sm.add_widget(SplashScreen(name='splash screen'))
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(PongGameScreen(name='pong game'))
        return sm

    def on_start(self):
        Window.size = (2556, 1179)

        screen_width = Window.width
        screen_height = Window.height
        window_width = self.root.width
        window_height = self.root.height

        x = screen_width - window_width / 2
        y = screen_height - window_height / 2

        Window.position = 'custom'
        Window.top = y
        Window.left = x

        Clock.schedule_once(self.change_screen, 3)

    def change_screen(self, *args):
        self.root.transition = FadeTransition(duration=0.25)
        self.root.current = 'login'


if __name__ == '__main__':
    GameApp().run()
