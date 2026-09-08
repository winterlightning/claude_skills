"""Symmetric domed octopus with four curling arms; no useful exact Lucide match."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9ff10113-0a7f-5f71-8a7b-84acf412169c'
SOURCE_PATH = 'pictographic-primitives/animals/octopus_9ff10113-0a7f-5f71-8a7b-84acf412169c.svg'
AUTHOR = 'gpt-6'


class Octopus(Solo48):
    icon_id = 'octopus'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('octopus',)

    def build(self) -> None:
        # Centerline extremes from SQUARE: (0, 0, 48, 48)
        self.add_arc('dome-left', (12, 16), (24, 2), radius_x=12, radius_y=14, sweep=True, large_arc=False)
        self.add_arc('dome-right', (24, 2), (36, 16), radius_x=12, radius_y=14, sweep=True, large_arc=False)
        self.add_line('side-right', (36, 16), (34, 27))
        self.add_arc('arm-right', (34, 27), (46, 27), radius_x=6, radius_y=6, sweep=False, large_arc=False)
        self.add_contour('upper', 'dome-left', 'dome-right', 'side-right', 'arm-right', closed=False)
        self.add_line('side-left', (12, 16), (14, 27))
        self.add_arc('arm-left', (14, 27), (2, 27), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_contour('left', 'side-left', 'arm-left', closed=False)
        self.relate("connect", 'upper', 'left')
        self.add_arc('inner-left', (20, 33), (8, 46), radius_x=12, radius_y=13, sweep=True, large_arc=False)
        self.add_arc('inner-right', (28, 33), (40, 46), radius_x=12, radius_y=13, sweep=False, large_arc=False)
