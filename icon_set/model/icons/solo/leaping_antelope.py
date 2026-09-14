# Review candidate; original preserved.
"""An antelope stretching diagonally into a leap."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '79daad3e-b421-490c-80f2-e08549dfba1b'
SOURCE_PATH = 'pictographic-primitives/animals/deer jump_79daad3e-b421-490c-80f2-e08549dfba1b.svg'
AUTHOR = 'gpt-6'

class LeapingAntelope(Solo48):
    icon_id = 'leaping-antelope'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('antelope', 'deer', 'leap', 'jump', 'running', 'gazelle', 'wildlife', 'motion')

    def build(self):
        # Leaping antelope: smooth back and belly, a compact head and single clean legs preserving the leap.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        a('back',(10,24),(22,14),12,10)
        p('neck',(22,14),(30,14),(34,8),(42,12),(38,18),(34,18),(30,28))
        a('belly',(30,28),(10,24),20,8)
        link('connect','back','neck')
        link('connect','neck','belly')
        link('connect','belly','back')
        p('rear-leg',(10,24),(6,34),(6,42))
        p('front-leg',(30,28),(42,22),(42,34))
        link('connect','rear-leg','back')
        link('connect','rear-leg','belly')
        link('connect','front-leg','neck')
        link('connect','front-leg','belly')
        p('horn',(34,8),(30,6),(24,6))
        link('connect','horn','neck')
