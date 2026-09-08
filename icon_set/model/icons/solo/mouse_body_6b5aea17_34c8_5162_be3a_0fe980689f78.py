"""Upright mouse with two rounded ears and haunch; eye and paw scoring omitted. Lucide rat informs ears."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6b5aea17-34c8-5162-be3a-0fe980689f78'
SOURCE_PATH = 'pictographic-primitives/animals/mouse body_6b5aea17-34c8-5162-be3a-0fe980689f78.svg'
AUTHOR = 'gpt-6'


class SittingMouse(Solo48):
    icon_id = 'sitting-mouse'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('sitting', 'mouse')

    def build(self) -> None:
        # Centerline extremes from VRECT_L: (6, 0, 42, 48)
        self.add_arc('ear-left-base', (18, 16), (10, 10), radius_x=8, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('ear-left', (10, 10), (24, 10), radius_x=7, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('ear-right', (24, 10), (38, 10), radius_x=7, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('ear-right-base', (38, 10), (34, 16), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_line('nose', (34, 16), (40, 22))
        self.add_arc('muzzle', (40, 22), (32, 28), radius_x=8, radius_y=6, sweep=True, large_arc=False)
        self.add_line('chest', (32, 28), (32, 34))
        self.add_arc('belly', (32, 34), (20, 46), radius_x=12, radius_y=12, sweep=True, large_arc=False)
        self.add_arc('rump', (20, 46), (8, 34), radius_x=12, radius_y=12, sweep=True, large_arc=False)
        self.add_arc('back', (8, 34), (18, 24), radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_line('neck', (18, 24), (18, 16))
        self.add_contour('mouse', 'ear-left-base', 'ear-left', 'ear-right', 'ear-right-base', 'nose', 'muzzle', 'chest', 'belly', 'rump', 'back', 'neck', closed=True)
        self.add_arc('tail', (32, 34), (40, 42), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.relate("connect", 'mouse', 'tail')
