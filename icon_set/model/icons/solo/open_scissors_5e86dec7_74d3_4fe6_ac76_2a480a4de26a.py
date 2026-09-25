"""Open scissors with outward-bowed blades and two circular finger loops; fine blade outlines and pivot dot omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5e86dec7-74d3-4fe6-ac76-2a480a4de26a'
SOURCE_PATH = 'pictographic-primitives/tools/scissors_5e86dec7-74d3-4fe6-ac76-2a480a4de26a.svg'
AUTHOR = 'gpt-6'

class OpenScissors(Solo48):
    icon_id = 'open-scissors'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'tools'
    aliases = ()
    keywords = ('scissors', 'cut', 'shears', 'blades', 'open', 'craft', 'tailor', 'tool')

    def build(self) -> None:
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.

        def circle(n, x, y, r):
            self.add_arc(n + '-a', (x - r, y), (x + r, y), radius_x=r)
            self.add_arc(n + '-b', (x + r, y), (x - r, y), radius_x=r)
            self.add_contour(n, n + '-a', n + '-b', closed=True)
        for n, x in [('left', 13), ('right', 35)]:
            circle(n + '-loop', x, 39, 5)
        self.add_line('neck-a', (13, 34), (24, 22))
        self.add_arc('bow-a', (24, 22), (36, 4), radius_x=18, sweep=False)
        self.add_contour('blade-a', 'neck-a', 'bow-a')
        self.add_line('neck-b', (35, 34), (24, 22))
        self.add_arc('bow-b', (24, 22), (12, 4), radius_x=18)
        self.add_contour('blade-b', 'neck-b', 'bow-b')
        self.relate('connect', 'blade-a', 'left-loop')
        self.relate('connect', 'blade-b', 'right-loop')
        self.relate('connect', 'blade-a', 'blade-b')
