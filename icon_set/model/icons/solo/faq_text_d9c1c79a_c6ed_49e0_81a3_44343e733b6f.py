"""FAQ Text. Keeps FAQ; uses a flat A cap to open its counter at native size.

HRECT_L visible extremes (2, 6, 46, 42), centerlines (4, 8, 44, 40).
Lucide type: coherent monoline letter strokes.
Geometry authored directly on SOLO48. Letter order and directional numerals
retain intentional asymmetry; repeated letters share construction parameters.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd9c1c79a-c6ed-49e0-81a3-44343e733b6f'
SOURCE_PATH = 'pictographic-primitives/symbol/FAQ_d9c1c79a-c6ed-49e0-81a3-44343e733b6f.svg'
AUTHOR = 'gpt-6'


class FaqText(Solo48):
    icon_id = 'faq-text'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'symbols/labels'
    aliases = ()
    keywords = ('faq', 'questions', 'help', 'support', 'answers', 'information', 'text')

    def build(self) -> None:
        self.add_polyline('f-stem', (8, 8), (6, 8), (6, 24), (6, 40))
        self.add_line('f-bar', (6, 24), (8, 24))
        self.relate("connect", 'f-stem', 'f-bar')
        self.add_polyline('a-arch', (16, 40), (16, 24), (16, 8), (26, 8), (26, 24), (26, 40))
        self.add_line('a-bar', (16, 24), (26, 24))
        self.relate("connect", 'a-arch', 'a-bar')
        self.add_arc('q-top', (36, 12), (42, 12), radius_x=4, radius_y=4, sweep=True)
        self.add_line('q-right', (42, 12), (42, 33))
        self.add_arc('q-bottom', (42, 33), (36, 33), radius_x=4, radius_y=4, sweep=True)
        self.add_line('q-left', (36, 33), (36, 12))
        self.add_contour('q', 'q-top', 'q-right', 'q-bottom', 'q-left', closed=True)
        self.add_line('q-tail', (40, 37), (42, 40))
        self.relate("connect", 'q', 'q-tail')
