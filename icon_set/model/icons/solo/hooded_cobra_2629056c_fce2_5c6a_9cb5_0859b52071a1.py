"""Rearing cobra with flared hood and wide base coil. Extrema (6,6)-(42,42). Shared hood radii preserve symmetry; tiny separate tail omitted. No useful Lucide match."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2629056c-fce2-5c6a-9cb5-0859b52071a1'
SOURCE_PATH = 'pictographic-primitives/animals/reptile cobra_2629056c-fce2-5c6a-9cb5-0859b52071a1.svg'
AUTHOR = 'gpt-6'

class HoodedCobra(Solo48):
    icon_id = 'hooded-cobra'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('cobra', 'snake', 'hood', 'reptile', 'serpent', 'coil', 'venom', 'rear')

    def build(self):
        # Symmetric hood uses radius-12 quarters; base coil has a full 8-unit centerline opening and radius-4 ends. Eye pair shares y=16. No useful Lucide cobra match.
        self.add_line('head-top', (18, 6), (30, 6))
        self.add_arc('hood-right', (30, 6), (42, 18), radius_x=12, radius_y=12, sweep=True)
        self.add_arc('taper-right', (42, 18), (30, 30), radius_x=12, radius_y=12, sweep=True)
        self.add_line('neck-right', (30, 30), (30, 34))
        self.add_line('coil-top-right', (30, 34), (38, 34))
        self.add_arc('coil-right', (38, 34), (38, 42), radius_x=4, radius_y=4, sweep=True)
        self.add_line('coil-bottom', (38, 42), (10, 42))
        self.add_arc('coil-left', (10, 42), (10, 34), radius_x=4, radius_y=4, sweep=True)
        self.add_line('coil-top-left', (10, 34), (18, 34))
        self.add_line('neck-left', (18, 34), (18, 30))
        self.add_arc('taper-left', (18, 30), (6, 18), radius_x=12, radius_y=12, sweep=True)
        self.add_arc('hood-left', (6, 18), (18, 6), radius_x=12, radius_y=12, sweep=True)
        self.add_contour('outline', 'head-top', 'hood-right', 'taper-right', 'neck-right', 'coil-top-right', 'coil-right', 'coil-bottom', 'coil-left', 'coil-top-left', 'neck-left', 'taper-left', 'hood-left', closed=True)
        self.add_dot('eye-left', (18, 16))
        self.add_dot('eye-right', (30, 16))
