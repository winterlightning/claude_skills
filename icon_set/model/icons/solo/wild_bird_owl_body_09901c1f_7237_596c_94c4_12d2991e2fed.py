"""standing-owl: source silhouette re-authored on SOLO48.

Lucide bird informs coherent body arcs and sparse detail.
Keyshape VRECT_L; extremes obtained from the SOLO48 contract.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '09901c1f-7237-596c-94c4-12d2991e2fed'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird owl body_09901c1f-7237-596c-94c4-12d2991e2fed.svg'
AUTHOR = 'gpt-6'


class StandingOwl(Solo48):
    icon_id = 'standing-owl'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/birds"
    aliases = ()
    keywords = ('owl', 'standing', 'wise', 'bird', 'night', 'feathers', 'nocturnal', 'perch')

    def build(self) -> None:
        self.add_line('tuft-left', (8, 2), (19, 7))
        self.add_arc('crown', (19, 7), (40, 20), radius_x=15, radius_y=15, sweep=True)
        self.add_arc('back', (40, 20), (26, 40), radius_x=20, radius_y=22, sweep=True)
        self.add_line('tail', (26, 40), (8, 40))
        self.add_arc('breast', (8, 40), (15, 19), radius_x=40, radius_y=40, sweep=True)
        self.add_line('forehead', (15, 19), (8, 2))
        self.add_contour('owl', 'tuft-left', 'crown', 'back', 'tail', 'breast', 'forehead', closed=True)
        self.add_line('tuft-right', (19, 7), (40, 2))
        self.relate("connect", 'owl', 'tuft-right')
        self.add_dot('eye-left', (22, 16))
        self.add_dot('eye-right', (31, 16))
        self.add_polyline('beak', (23, 24), (26, 27), (29, 24))
        self.add_line('leg', (26, 40), (29, 46))
        self.add_line('foot', (29, 46), (35, 46))
        self.add_contour('perch', 'leg', 'foot', closed=False)
        self.relate("connect", 'owl', 'perch')
