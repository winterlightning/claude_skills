"""Rattlesnake with broad U bends, tapering head and rattle dashes. Extrema (2,2)-(46,46). Smooth paired bends replace source switchbacks; small tongue fork omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd4648896-3720-5e11-b38e-0b0c450735c6'
SOURCE_PATH = 'pictographic-primitives/animals/reptile rattlesnake_d4648896-3720-5e11-b38e-0b0c450735c6.svg'
AUTHOR = 'gpt-6'


class Rattlesnake(Solo48):
    icon_id = 'rattlesnake'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals/reptiles'
    aliases = ()
    keywords = ('rattlesnake', 'snake', 'rattle', 'reptile', 'slither', 'venom', 'desert', 'serpent')

    def build(self) -> None:
        # Rattlesnake with broad U bends, tapering head and rattle dashes. Extrema (2,2)-(46,46). Smooth paired bends replace source switchbacks; small tongue fork omitted.
        self.add_line('tail-outer', (2, 25), (2, 32))
        self.add_arc('bend-outer', (2, 32), (26, 32), radius_x=12, radius_y=12, sweep=False)
        self.add_line('rise-right', (26, 32), (26, 12))
        self.add_arc('top-inner', (26, 12), (34, 12), radius_x=4, radius_y=4, sweep=True)
        self.add_line('head-neck', (34, 12), (34, 22))
        self.add_arc('head-left', (34, 22), (34, 32), radius_x=10, radius_y=10, sweep=False)
        self.add_arc('head-taper-left', (34, 32), (40, 42), radius_x=6, radius_y=10, sweep=False)
        self.add_arc('head-taper-right', (40, 42), (46, 32), radius_x=6, radius_y=10, sweep=False)
        self.add_arc('head-right', (46, 32), (42, 22), radius_x=4, radius_y=10, sweep=False)
        self.add_line('rise-outer', (42, 22), (42, 14))
        self.add_arc('top-outer', (42, 14), (18, 14), radius_x=12, radius_y=12, sweep=False)
        self.add_line('fall-left', (18, 14), (18, 32))
        self.add_arc('bend-inner', (18, 32), (10, 32), radius_x=4, radius_y=4, sweep=True)
        self.add_line('tail-inner', (10, 32), (10, 25))
        self.add_arc('tail-cap', (10, 25), (2, 25), radius_x=4, radius_y=4, sweep=False)
        self.add_contour('snake', 'tail-outer', 'bend-outer', 'rise-right', 'top-inner', 'head-neck', 'head-left', 'head-taper-left', 'head-taper-right', 'head-right', 'rise-outer', 'top-outer', 'fall-left', 'bend-inner', 'tail-inner', 'tail-cap')
        self.add_line('rattle-top', (5, 4), (7, 4))
        self.add_line('rattle-bottom', (4, 12), (8, 12))
        self.add_line('tongue', (40, 42), (40, 46))
        self.relate("connect", 'snake', 'tongue')
