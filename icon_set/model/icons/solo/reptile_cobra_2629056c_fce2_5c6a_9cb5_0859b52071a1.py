"""Rearing cobra with flared hood and wide base coil. Extrema (6,6)-(42,42). Shared hood radii preserve symmetry; tiny separate tail omitted. No useful Lucide match."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2629056c-fce2-5c6a-9cb5-0859b52071a1'
SOURCE_PATH = 'pictographic-primitives/animals/reptile cobra_2629056c-fce2-5c6a-9cb5-0859b52071a1.svg'
AUTHOR = 'gpt-6'


class HoodedCobra(Solo48):
    icon_id = 'hooded-cobra'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals/reptiles'
    aliases = ()
    keywords = ('cobra', 'snake', 'hood', 'reptile', 'serpent', 'coil', 'venom', 'rear')

    def build(self) -> None:
        # Rearing cobra with flared hood and wide base coil. Extrema (6,6)-(42,42). Shared hood radii preserve symmetry; tiny separate tail omitted. No useful Lucide match.
        self.add_line('hood-top', (18, 6), (30, 6))
        self.add_arc('hood-right', (30, 6), (42, 14), radius_x=12, radius_y=12, sweep=True)
        self.add_arc('hood-taper-right', (42, 14), (36, 25), radius_x=14, radius_y=14, sweep=True)
        self.add_arc('neck-right', (36, 25), (30, 36), radius_x=14, radius_y=14, sweep=False)
        self.add_line('body-right', (30, 36), (30, 38))
        self.add_line('coil-top-right', (30, 38), (42, 38))
        self.add_arc('coil-end', (42, 38), (42, 42), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('coil-bottom-end', (42, 42), (42, 42), radius_x=4, radius_y=4, sweep=True)
        self.add_line('coil-bottom', (42, 42), (6, 42))
        self.add_arc('coil-left', (6, 42), (6, 42), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('coil-upper-left', (6, 42), (6, 38), radius_x=4, radius_y=4, sweep=True)
        self.add_line('coil-top-left', (6, 38), (18, 38))
        self.add_line('body-left', (18, 38), (18, 36))
        self.add_arc('neck-left', (18, 36), (12, 25), radius_x=14, radius_y=14, sweep=False)
        self.add_arc('hood-taper-left', (12, 25), (6, 14), radius_x=14, radius_y=14, sweep=True)
        self.add_arc('hood-left', (6, 14), (18, 6), radius_x=12, radius_y=12, sweep=True)
        self.add_contour('outline', 'hood-top', 'hood-right', 'hood-taper-right', 'neck-right', 'body-right', 'coil-top-right', 'coil-end', 'coil-bottom-end', 'coil-bottom', 'coil-left', 'coil-upper-left', 'coil-top-left', 'body-left', 'neck-left', 'hood-taper-left', 'hood-left')
        self.add_dot('eye-left', (18, 14))
        self.add_dot('eye-right', (30, 14))
