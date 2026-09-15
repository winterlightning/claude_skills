"""perching-bird: source silhouette re-authored on SOLO48.

Lucide bird informs coherent body arcs and sparse detail.
Keyshape VRECT_XL; extremes obtained from the SOLO48 contract.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0f8fae80-7c30-4fdb-9d48-8b632249f687'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird_0f8fae80-7c30-4fdb-9d48-8b632249f687.svg'
AUTHOR = 'gpt-6'


class PerchingBird(Solo48):
    icon_id = 'perching-bird'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/birds"
    aliases = ()
    keywords = ('bird', 'perching', 'songbird', 'wing', 'beak', 'tail', 'garden', 'wildlife')

    def build(self) -> None:
        self.add_line('beak', (6, 10), (13, 6))
        self.add_bezier('head-a', (13, 6), *(((15.47520861, 6), (18.52479139, 6), (21, 6)),))
        self.add_bezier('head-b', (21, 6), *(((24.2325716, 6), (27.39737339, 7.16125546), (29, 10)),))
        self.add_line('back', (29, 10), (42, 38))
        self.add_arc('belly', (42, 38), (35, 40), radius_x=17, radius_y=17, sweep=True)
        self.add_line('underside', (35, 40), (27, 40))
        self.add_arc('breast', (27, 40), (11, 24), radius_x=16, radius_y=16, sweep=True)
        self.add_line('forehead', (11, 24), (11, 7))
        self.add_contour('body', 'head-a', 'head-b', 'back', 'belly', 'underside', 'breast', 'forehead', closed=False)
        self.relate("connect", 'body', 'beak')
        self.add_arc('wing', (21, 16), (42, 38), radius_x=22, radius_y=22, sweep=False)
        self.relate("connect", 'body', 'wing')
        self.add_line('tail', (42, 38), (42, 42))
        self.relate("connect", 'body', 'tail')
        self.add_line('leg-left', (27, 40), (24, 42))
        self.add_line('leg-right', (35, 40), (34, 42))
        self.relate("connect", 'body', 'leg-left')
        self.relate("connect", 'body', 'leg-right')
