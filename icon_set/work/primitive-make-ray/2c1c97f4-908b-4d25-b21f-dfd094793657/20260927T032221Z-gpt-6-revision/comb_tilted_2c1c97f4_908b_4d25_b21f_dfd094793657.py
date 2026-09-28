"""Comb. Retains three parallel teeth and the tilted spine with end feet.

VRECT_L visible extremes (6, 2, 42, 46); centerlines (8, 4, 40, 44).
Supplied reference; no useful exact Lucide match found.
Repeated teeth share a slanted rhythm and the spine ends have short curves.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '2c1c97f4-908b-4d25-b21f-dfd094793657'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__comb-tilted/20260927T032022Z-thuan-mac-1/reference/comb_2c1c97f4-908b-4d25-b21f-dfd094793657.svg'
AUTHOR = "gpt-6"


class CombTilted(Solo48):
    icon_id = 'comb-tilted'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol",)
    aliases = ()
    keywords = ('comb', 'hair', 'grooming', 'barber', 'beauty', 'brush', 'salon', 'care')

    def build(self) -> None:
        # Curved head and heel replace the rejected comb's blunt angular ends.
        self.add_line('spine-head-line', (20, 4), (36, 10))
        self.add_arc('spine-head-corner', (36, 10), (40, 12), radius_x=4, sweep=False)
        self.add_line('spine-a', (40, 12), (37, 20))
        self.add_line('spine-b', (37, 20), (34, 28))
        self.add_line('spine-c', (34, 28), (31, 36))
        self.add_line('spine-d', (31, 36), (28, 44))
        self.add_line('spine-heel-line', (28, 44), (12, 38))
        self.add_arc('spine-heel-cap', (12, 38), (8, 36), radius_x=4, sweep=False)
        self.add_contour('spine', 'spine-head-line', 'spine-head-corner',
                         'spine-a', 'spine-b', 'spine-c', 'spine-d',
                         'spine-heel-line', 'spine-heel-cap')
        self.add_line('tooth-one', (37, 20), (22, 14))
        self.relate("connect", 'spine', 'tooth-one')
        self.add_line('tooth-two', (34, 28), (19, 22))
        self.relate("connect", 'spine', 'tooth-two')
        self.add_line('tooth-three', (31, 36), (16, 30))
        self.relate("connect", 'spine', 'tooth-three')
