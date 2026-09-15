'T-shirt: symmetric sleeves, a smooth neckline and clear 8-unit sleeve widths.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c5bf3209-ac20-4f1c-90e6-36bb732043c1'
SOURCE_PATH = 'pictographic-primitives/clothes/t shirt_c5bf3209-ac20-4f1c-90e6-36bb732043c1.svg'
AUTHOR = 'gpt-6'

class TShirtC5bf3209(Solo48):
    icon_id = 't-shirt-c5bf3209'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    aliases = ()
    keywords = ('t', 'shirt', 'clothes')

    def build(self):
        # T-shirt: symmetric sleeves, a smooth neckline and clear 8-unit sleeve widths.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        l('shoulder-left',(14,6),(18,6))
        a('neck',(18,6),(30,6),6,sweep=False)
        l('shoulder-right',(30,6),(34,6))
        p('right',(34,6),(42,14),(42,24),(34,24),(34,42),(14,42),(14,24),(6,24),(6,14),(14,6))
        link('connect','shoulder-left','neck')
        link('connect','shoulder-right','neck')
        link('connect','right','shoulder-left')
        link('connect','right','shoulder-right')
        l('sleeve-left',(14,16),(14,24))
        l('sleeve-right',(34,16),(34,24))
        link('connect','sleeve-left','right')
        link('connect','sleeve-right','right')
