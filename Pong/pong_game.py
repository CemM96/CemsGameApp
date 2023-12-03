from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from random import randint
from kivy.clock import Clock


class PongPaddle(Widget):
    """
    Defines the paddle for the Pong game.
    """

    def bounce_ball(self, ball):
        """
        Handles the ball's interaction with the paddle.
        """
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            new_vx = -1.5 * vx
            ball.x = self.x - ball.width if vx > 0 else self.right
            ball.velocity = new_vx, vy


class PongBall(Widget):
    """
    Defines the ball for the Pong game.
    """
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        """
        Updates the position of the ball.
        """
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):
    """
    Main game class for Pong.
    """
    ball = ObjectProperty(None)
    player_1 = ObjectProperty(None)
    player_2 = ObjectProperty(None)
    player_1_score = NumericProperty(0)
    player_2_score = NumericProperty(0)

    def serve_ball(self):
        """
        Serves the ball at the start or after a score.
        """
        self.ball.center = self.center
        angle = randint(0, 359)
        while any([60 <= angle <= 120, 240 <= angle <= 300, 0 <= angle <= 30, 330 <= angle <= 359, 150 <= angle <= 210]):
            angle = randint(0, 359)
        self.ball.velocity = Vector(12, 0).rotate(angle)

    def serve_button_pressed(self):
        """
        Handles the serve button press action.
        """
        self.ids.exit_button.opacity = 0
        self.ids.exit_button.disabled = True
        self.ids.serve_button.opacity = 0
        self.ids.serve_button.disabled = True
        self.ball.velocity = Vector(0, 0)
        Clock.schedule_interval(self.update, 1.0 / 60.0)
        Clock.schedule_once(lambda dt: self.serve_ball(), 0.8)

    def end_game(self):
        """
        Ends the game and resets the scores.
        """
        self.player_1_score = 0
        self.player_2_score = 0
        self.reset_game_state()

    def reset_game_state(self):
        """
        Resets the game state.
        """
        self.ball.center = self.center
        self.ball.velocity = Vector(0, 0)
        Clock.unschedule(self.update)
        self.ids.exit_button.opacity = 1
        self.ids.exit_button.disabled = False
        self.ids.serve_button.opacity = 1
        self.ids.serve_button.disabled = False

    def update(self, dt):
        """
        Updates the game state.
        """
        self.ball.move()
        self.handle_ball_collisions()
        self.check_scores()

    def handle_ball_collisions(self):
        """
        Handles collisions of the ball with walls and paddles.
        """
        if self.ball.y < 0 or self.ball.y > self.height - 50:
            self.ball.velocity_y *= -1

        if self.ball.x < 0:
            self.score_point(player='player_2')

        if self.ball.x > self.width - 50:
            self.score_point(player='player_1')

        self.player_1.bounce_ball(self.ball)
        self.player_2.bounce_ball(self.ball)

    def score_point(self, player):
        """
        Increments the score for the given player and resets the game state.
        """
        if player == 'player_1':
            self.player_1_score += 1
        elif player == 'player_2':
            self.player_2_score += 1
        self.reset_game_state()

    def check_scores(self):
        """
        Checks if any player has won the game.
        """
        if self.player_1_score == 10 or self.player_2_score == 10:
            self.end_game()

    def on_touch_move(self, touch):
        """
        Handles touch movement for player controls.
        """
        if touch.x < self.width / 4:
            self.player_1.center_y = touch.y
        elif touch.x > self.width * 3 / 4:
            self.player_2.center_y = touch.y
