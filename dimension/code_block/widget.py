import pdb

from kivy.uix.widget import Widget
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import BooleanProperty, ReferenceListProperty, NumericProperty, ObjectProperty


class CodeBlock(FloatLayout):
    scatter = ObjectProperty(None)
    selected = BooleanProperty(False)
    default_width = NumericProperty(0)
    default_height = NumericProperty(0)
    default_size = ReferenceListProperty(default_width, default_height)
    scale_factor = NumericProperty(0)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.selected = True
        return super(CodeBlock, self).on_touch_down(touch)

    def on_touch_up(self, touch):
        self.selected = False
        return super(CodeBlock, self).on_touch_up(touch)

    # def on_touch_move(self, touch):
    #     if super(CodeBlock, self).on_touch_move(touch):
    #         if self.selected:
    #             self.center = self.center_x + touch.dx, self.center_y + touch.dy
    #     return None

    def apply_transform(self, *args, **kwargs):
        self.scatter.apply_transform(*args, **kwargs)
