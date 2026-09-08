"""Profile mouse with long doubled-back tail; Lucide rat informs continuous tail and rounded body."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5de17e52-807d-512f-bec7-d16365517673'
SOURCE_PATH = 'pictographic-primitives/animals/mouse tail_5de17e52-807d-512f-bec7-d16365517673.svg'
AUTHOR = 'gpt-6'


class MouseWithLongTail(Solo48):
    icon_id = 'mouse-with-long-tail'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('mouse', 'with', 'long', 'tail')

    def build(self) -> None:
        # Centerline extremes from SQUARE: (0, 0, 48, 48)
        self.add_arc('back', (20, 12), (8, 24), radius_x=12, radius_y=12, sweep=False, large_arc=False)
        self.add_arc('rump', (8, 24), (18, 34), radius_x=10, radius_y=10, sweep=False, large_arc=False)
        self.add_line('belly', (18, 34), (32, 34))
        self.add_line('chest', (32, 34), (34, 24))
        self.add_arc('snout', (34, 24), (46, 16), radius_x=12, radius_y=8, sweep=False, large_arc=False)
        self.add_line('face', (46, 16), (36, 12))
        self.add_arc('ear', (36, 12), (24, 12), radius_x=6, radius_y=10, sweep=False, large_arc=True)
        self.add_contour('mouse', 'back', 'rump', 'belly', 'chest', 'snout', 'face', 'ear', closed=False)
        self.add_arc('tail-turn', (8, 24), (8, 40), radius_x=6, radius_y=8, sweep=False, large_arc=False)
        self.add_line('tail-run', (8, 40), (26, 40))
        self.add_arc('tail-tip', (26, 40), (26, 46), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('tail-end', (26, 46), (16, 46))
        self.add_contour('tail', 'tail-turn', 'tail-run', 'tail-tip', 'tail-end', closed=False)
        self.relate("connect", 'mouse', 'tail')
