"""Broccoli and Carrot. Keeps both vegetables and a leaf fork; reduces broccoli stalk to one stroke and omits carrot grooves.

SQUARE visible extremes (4, 4, 44, 44); centerlines (6, 6, 42, 42).
Lucide carrot: broad tapered root and simple leaf cluster; supplied source determines broccoli and overlap.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1833535f-220e-490a-9e51-7058a14ac9db'
SOURCE_PATH = 'pictographic-primitives/symbol/broccoli carrot_1833535f-220e-490a-9e51-7058a14ac9db.svg'
AUTHOR = 'gpt-6'


class BroccoliAndCarrot(Solo48):
    icon_id = 'broccoli-and-carrot'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol",)
    aliases = ()
    keywords = ('broccoli', 'carrot', 'vegetables', 'food', 'healthy', 'vegan', 'groceries', 'produce')

    def build(self) -> None:
        self.add_arc('crown-left', (12, 24), (6, 18), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('crown-nw', (6, 18), (12, 10), radius_x=6, radius_y=8, sweep=True)
        self.add_arc('crown-top', (12, 10), (20, 10), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('crown-ne', (20, 10), (24, 16), radius_x=4, radius_y=6, sweep=True)
        self.add_arc('crown-right', (24, 16), (18, 24), radius_x=6, radius_y=8, sweep=True)
        self.add_line('crown-base-1', (18, 24), (15, 23))
        self.add_line('crown-base-2', (15, 23), (12, 24))
        self.add_contour('broccoli', 'crown-left', 'crown-nw', 'crown-top', 'crown-ne', 'crown-right', 'crown-base-1', 'crown-base-2', closed=True)
        self.add_line('stem', (12, 24), (14, 34))
        self.relate("connect", 'broccoli', 'stem')
        self.add_line('carrot-left', (20, 42), (30, 26))
        self.add_arc('carrot-cap-a', (30, 26), (36, 28), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('carrot-cap-b', (36, 28), (40, 36), radius_x=10, radius_y=10, sweep=True)
        self.add_line('carrot-right', (40, 36), (20, 42))
        self.add_contour('carrot', 'carrot-left', 'carrot-cap-a', 'carrot-cap-b', 'carrot-right', closed=True)
        self.add_polyline('leaves', (38, 16), (38, 26), (42, 22))
        self.add_line('leaf-stem', (38, 26), (36, 28))
        self.relate("connect", 'carrot', 'leaf-stem')
        self.relate("connect", 'leaves', 'leaf-stem')
