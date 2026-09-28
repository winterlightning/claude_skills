"""An oversized hand reaches in from the upper left and pinches the top of a small person's head. The suspended figure has a rounded head, straight arms and two short separated legs.
Lucide hand/pointer construction; no exact match. Opposing fingers physically pinch the small head. Figure reduced to round head and joined limbs; finger creases omitted. Asymmetric reaching hand retained.
SQUARE: centerline extremes (6,6)-(42,42); freshly authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1236a37e-46a5-4aeb-8418-b30644f987bb'
SOURCE_PATH = 'pictographic-primitives/work/worker lay off fired user pick drop_1236a37e-46a5-4aeb-8418-b30644f987bb.svg'
AUTHOR = 'gpt-6'


class HandPickingUpPerson(Solo48):
    icon_id = 'hand-picking-up-person'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "work"
    categories = ("work", "primitives")
    aliases = ()
    keywords = ('hand', 'person', 'picking', 'holding', 'worker', 'selection')

    def build(self) -> None:
        self.add_arc('head-left', (30, 30), (30, 22), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('head-right', (30, 22), (30, 30), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('neck', (30, 30), (30, 39))
        self.add_contour('head-and-torso', 'head-left', 'head-right', 'neck', closed=False)
        self.add_polyline('arms', (18, 39), (30, 39), (42, 39), closed=False)
        self.relate("connect", 'arms', 'head-and-torso')
        self.add_polyline('legs', (22, 42), (30, 39), (38, 42), closed=False)
        self.relate("connect", 'legs', 'arms')
        self.relate("connect", 'legs', 'head-and-torso')
        self.add_polyline('hand-top', (6, 6), (28, 6), (40, 12), closed=False)
        self.add_arc('finger-round', (40, 12), (36, 18), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('finger-slope', (36, 18), (32, 14))
        self.add_line('finger-upper', (32, 14), (26, 14))
        self.add_arc('pinch', (26, 14), (26, 22), radius_x=4, radius_y=4, sweep=False, large_arc=False)
        self.add_line('finger-lower', (26, 22), (30, 22))
        self.add_contour('finger-inner', 'finger-slope', 'finger-upper', 'pinch', 'finger-lower', closed=False)
        self.relate("connect", 'hand-top', 'finger-round')
        self.relate("connect", 'finger-round', 'finger-inner')
        self.relate("connect", 'finger-inner', 'head-and-torso')
        self.add_polyline('hand-bottom', (6, 16), (12, 16), (20, 26), (26, 26), closed=False)
        self.relate("connect", 'hand-bottom', 'head-and-torso')
