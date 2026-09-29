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
    category = "animals"
    categories = ("animals", "primitives")
    aliases = ()
    keywords = ('octopus',)

    def build(self) -> None:
        # Centerline extremes from SQUARE: (0, 0, 48, 48)
        self.add_bezier('dome-left', (12, 16), *(((13.56542937, 9.85418684), (18.50920143, 6), (24, 6)),))
        self.add_bezier('dome-right', (24, 6), *(((29.49079857, 6), (34.43457063, 9.85418684), (36, 16)),))
        self.add_line('side-right', (36, 16), (34, 27))
        self.add_arc('arm-right', (34, 27), (42, 27), radius_x=6, radius_y=6, sweep=False, large_arc=False)
        self.add_contour('upper', 'dome-left', 'dome-right', 'side-right', 'arm-right', closed=False)
        self.add_line('side-left', (12, 16), (14, 27))
        self.add_arc('arm-left', (14, 27), (6, 27), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_contour('left', 'side-left', 'arm-left', closed=False)
        self.relate("connect", 'upper', 'left')
        self.add_bezier('inner-left', (20, 33), *(((18.33731217, 38.59330912), (13.41788519, 42), (8, 42)),))
        self.add_bezier('inner-right', (28, 33), *(((29.66268783, 38.59330912), (34.58211481, 42), (40, 42)),))
