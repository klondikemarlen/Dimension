import pdb

from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.properties import BooleanProperty, ReferenceListProperty, NumericProperty


class CodeBlock(Widget):
    selected = BooleanProperty(False)
    default_width = NumericProperty(0)
    default_height = NumericProperty(0)
    default_size = ReferenceListProperty(default_width, default_height)
    scale_factor = NumericProperty(0)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.selected = True
            return True

    def on_touch_up(self, touch):
        self.selected = False

    def on_touch_move(self, touch):
        if self.selected:
            self.center = self.center_x + touch.dx, self.center_y + touch.dy