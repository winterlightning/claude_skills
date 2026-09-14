# Review candidate; original preserved.
"""seal-balancing-ball: SQUARE ink (6,6)-(42,42). Raised head below plain ball; eye omitted for clearance."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '51d0c88f-615f-440d-bdfa-7172f9404ea7'
SOURCE_PATH = 'pictographic-primitives/animals/seal ball_51d0c88f-615f-440d-bdfa-7172f9404ea7.svg'
AUTHOR = 'gpt-6'

class SealBalancingBall(Solo48):
    icon_id = 'seal-balancing-ball'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals/marine'
    aliases = ()
    keywords = ('seal', 'ball', 'balance', 'circus', 'sea lion', 'trick', 'show', 'marine')

    def build(self):
        # Balancing seal: round ball and smooth upright body, with a single diagonal flipper.
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

        c('ball',14,12,6)
        a('head',(6,26),(22,26),8)
        l('neck',(22,26),(22,33))
        a('back',(22,33),(42,42),20,9)
        l('base',(42,42),(16,42))
        a('chest',(16,42),(6,32),10)
        l('front',(6,32),(6,26))
        self.add_contour('seal','head','neck','back','base','chest','front',closed=True)
        l('flipper',(16,34),(28,42))
        link('connect','flipper','seal')
        link('connect','ball','seal')
