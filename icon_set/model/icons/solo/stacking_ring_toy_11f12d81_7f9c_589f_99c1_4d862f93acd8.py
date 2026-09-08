"""A bear crown on four widening rounded rings. Shared tier boundaries avoid doubled strokes; facial decoration is omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '11f12d81-7f9c-589f-99c1-4d862f93acd8'
SOURCE_PATH = 'pictographic-primitives/babies/toy_11f12d81-7f9c-589f-99c1-4d862f93acd8.svg'
AUTHOR = 'gpt-6'


class StackingRingToy(Solo48):
    icon_id = 'stacking-ring-toy'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/babies"
    aliases = ()
    keywords = ('stacking', 'ring', 'toy', 'infant', 'nursery')

    def build(self) -> None:
        # Centerline extremes: (5,2)-(43,46).
        self.add_arc('ear-left', (16, 5), (22, 5), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('crown', (22, 5), (26, 5))
        self.add_arc('ear-right', (26, 5), (32, 5), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('cheek-right', (32, 5), (32, 8))
        self.add_arc('jaw-right', (32, 8), (26, 14), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_line('chin', (26, 14), (22, 14))
        self.add_arc('jaw-left', (22, 14), (16, 8), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_line('cheek-left', (16, 8), (16, 5))
        self.add_contour('bear', 'ear-left', 'crown', 'ear-right', 'cheek-right', 'jaw-right', 'chin', 'jaw-left', 'cheek-left', closed=True)
        self.add_line('ring-one-top', (16, 14), (32, 14))
        self.add_arc('ring-one-right', (32, 14), (32, 22), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('ring-one-bottom', (32, 22), (16, 22))
        self.add_arc('ring-one-left', (16, 22), (16, 14), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('ring-one', 'ring-one-top', 'ring-one-right', 'ring-one-bottom', 'ring-one-left', closed=True)
        self.add_line('ring-two-top', (14, 22), (34, 22))
        self.add_arc('ring-two-right', (34, 22), (34, 30), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('ring-two-bottom', (34, 30), (14, 30))
        self.add_arc('ring-two-left', (14, 30), (14, 22), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('ring-two', 'ring-two-top', 'ring-two-right', 'ring-two-bottom', 'ring-two-left', closed=True)
        self.add_line('ring-three-top', (12, 30), (36, 30))
        self.add_arc('ring-three-right', (36, 30), (36, 38), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('ring-three-bottom', (36, 38), (12, 38))
        self.add_arc('ring-three-left', (12, 38), (12, 30), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('ring-three', 'ring-three-top', 'ring-three-right', 'ring-three-bottom', 'ring-three-left', closed=True)
        self.add_line('ring-four-top', (9, 38), (39, 38))
        self.add_arc('ring-four-right', (39, 38), (39, 46), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('ring-four-bottom', (39, 46), (9, 46))
        self.add_arc('ring-four-left', (9, 46), (9, 38), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('ring-four', 'ring-four-top', 'ring-four-right', 'ring-four-bottom', 'ring-four-left', closed=True)
        self.relate("connect", 'bear', 'ring-one')
        self.relate("connect", 'ring-one', 'ring-two')
        self.relate("connect", 'ring-two', 'ring-three')
        self.relate("connect", 'ring-three', 'ring-four')
