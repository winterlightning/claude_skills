'Variable font: paired T forms with consistent stems and a balanced slider.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'de8c9243-bc9c-4c89-8720-203c0db986ff'
SOURCE_PATH = 'icons-json/interface-essential/variable font_de8c9243-bc9c-4c89-8720-203c0db986ff.json'
AUTHOR = 'gpt-6'

class VariableFont(Solo48):
    icon_id = 'variable-font'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('variable', 'font', 'interface-essential')

    def build(self):
        # Variable font: paired T forms with consistent stems and a balanced slider.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        def c(name, x, y, radius):
            a(name+'-top', (x-radius,y), (x+radius,y), radius)
            a(name+'-bottom', (x+radius,y), (x-radius,y), radius)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)

        for x in (12,36):
            p(f'top-{x}',(x-8,12),(x-8,8),(x+8,8),(x+8,12))
            l(f'stem-{x}',(x,8),(x,24))
            l(f'foot-{x}',(x-4,24),(x+4,24))
            link('connect',f'top-{x}',f'stem-{x}')
            link('connect',f'stem-{x}',f'foot-{x}')
        l('slider-left',(4,35),(19,35))
        l('slider-right',(29,35),(44,35))
        c('knob',24,35,5)
        link('connect','knob','slider-left')
        link('connect','knob','slider-right')
