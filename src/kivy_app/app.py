import random
from kivy.app import App
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector


class MouseGame(Widget):
    circle = ObjectProperty(None)

    def update(self):
        x = random.randint(self.circle.width, self.width - self.circle.width)
        y = random.randint(self.circle.height, self.height - self.circle.height)
        self.circle.pos = Vector(x, y)

    def on_touch_down(self, touch):
        if self.circle.pos[0] <= touch.pos[0] <= self.circle.pos[0] + self.circle.width and \
                self.circle.pos[1] <= touch.pos[1] <= self.circle.pos[1] + self.circle.height:
            # TODO: processing data and draw hot spot distribution map
            self.update()


class MouseApp(App):
    def build(self):
        game = MouseGame()
        return game


class Circle(Widget):
    pass
