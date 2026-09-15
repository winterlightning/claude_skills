"""A front-facing bust has a rounded lower face topped by a jagged crown-like opening. A curved band crosses the upper head, short rays flank it, and a small vertical mark sits on the chest.
Lucide user shoulder construction; no exact stress-head match. Jagged opening and band retained; chest mark and extra rays omitted to protect space. Symmetric.
SQUARE: centerline extremes (6,6)-(42,42); independently authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a909b542-9eea-596a-b3f1-76f310afb7f5'
SOURCE_PATH = 'pictographic-primitives/work/human resources employee stress_a909b542-9eea-596a-b3f1-76f310afb7f5.svg'
AUTHOR = 'gpt-6'


class PersonWithJaggedOpenHead(Solo48):
    icon_id = 'person-with-jagged-open-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/work"
    aliases = ()
    keywords = ('person', 'head', 'stress', 'employee', 'bust', 'pressure')

    def build(self) -> None:
        self.add_polyline('crown', (15, 18), (15, 6), (20, 10), (24, 6), (28, 10), (33, 6), (33, 18), closed=False)
        self.add_arc('jaw', (33, 18), (15, 18), radius_x=9, radius_y=9, sweep=True, large_arc=False)
        self.relate("connect", 'crown', 'jaw')
        self.add_line('band', (15, 18), (33, 18))
        self.relate("connect", 'band', 'crown')
        self.relate("connect", 'band', 'jaw')
        self.add_dot('ray-left', (6, 16))
        self.add_dot('ray-right', (42, 16))
        self.add_arc('shoulder-left', (6, 42), (14, 37), radius_x=8, radius_y=5, sweep=True, large_arc=False)
        self.add_line('shoulder-top', (14, 37), (34, 37))
        self.add_arc('shoulder-right', (34, 37), (42, 42), radius_x=8, radius_y=5, sweep=True, large_arc=False)
        self.add_contour('shoulders', 'shoulder-left', 'shoulder-top', 'shoulder-right', closed=False)
