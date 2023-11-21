from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from random import randint
from kivy.clock import Clock


class PongPaddle(Widget):

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            ball.velocity_x *= -1.2


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):

    ball = ObjectProperty(None)
    player_1 = ObjectProperty(None)
    player_2 = ObjectProperty(None)
    player_1_score = NumericProperty(0)
    player_2_score = NumericProperty(0)

    def serve_ball(self):

        self.ball.center = self.center

        while True:
            angle = randint(0, 359)
            if (
                    not (60 <= angle <= 120)
                    and not (240 <= angle <= 300)
                    and not (0 <= angle <= 30)
                    and not (330 <= angle <= 359)
                    and not (150 <= angle <= 210)
            ):
                break

        self.ball.velocity = Vector(8, 0).rotate(angle)

    def serve_button_pressed(self):
        self.ids.exit_button.opacity = 0
        self.ids.exit_button.disabled = True

        self.ids.serve_button.opacity = 0
        self.ids.serve_button.disabled = True

        Clock.schedule_once(lambda dt: self.serve_ball(), 0.8)

    def update(self, dt):

        self.ball.move()

        if (self.ball.y < 0) or (self.ball.y > self.height - 50):
            self.ball.velocity_y *= -1

        if self.ball.x < 0:
            self.ball.center = self.center
            self.ball.velocity = Vector(0, 0)
            self.player_1_score += 1
            self.serve_button_pressed()

        if self.ball.x > self.width - 50:
            self.ball.center = self.center
            self.ball.velocity = Vector(0, 0)
            self.player_2_score += 1
            self.serve_button_pressed()

        self.player_1.bounce_ball(self.ball)
        self.player_2.bounce_ball(self.ball)

    def on_touch_move(self, touch):
        if touch.x < self.width / 4:
            self.player_1.center_y = touch.y
        if touch.x > self.width * 3/4:
            self.player_2.center_y = touch.y
