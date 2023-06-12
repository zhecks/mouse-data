import random
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector
from src.data.data import Data


class MouseGame(Widget):
    data = Data()
    circle = ObjectProperty(None)
    rect = ObjectProperty(None)
    total = ObjectProperty(data.total)

    def update(self):
        x = random.randint(self.rect.pos[0], self.rect.pos[0] + self.rect.width - self.circle.width)
        y = random.randint(self.rect.pos[1], self.rect.pos[1] + self.rect.height - self.circle.height)
        self.circle.pos = Vector(x, y)

    def on_stop(self):
        self.data.process(self.width, self.height)

    def on_touch_down(self, touch):
        if self.circle.pos[0] <= touch.pos[0] <= self.circle.pos[0] + self.circle.width and \
                self.circle.pos[1] <= touch.pos[1] <= self.circle.pos[1] + self.circle.height:
            self.data.add_raw_position(touch.pos)
            self.update()
            self.total = self.total + 1


class MouseApp(App):
    game: MouseGame

    def build(self):
        self.game = MouseGame()
        return self.game

    def on_stop(self):
        self.game.on_stop()


class Circle(Widget):
    pass


class Rect(Widget):
    pass
