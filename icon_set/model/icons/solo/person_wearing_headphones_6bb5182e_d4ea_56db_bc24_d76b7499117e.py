"""A front-facing head and shoulder bust wears over-ear headphones. The band curves over the oval head, two earcups sit at the sides, and the shoulders broaden into a flat-bottomed torso.
Lucide headphones semicircular band and paired earcups. Inner top head contour and closed torso base omitted to avoid doubled tight curves; open jaw and shoulders retain the wearer.
VRECT_L: centerline extremes (8,6)-(40,42); independently authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6bb5182e-d4ea-56db-bc24-d76b7499117e'
SOURCE_PATH = 'pictographic-primitives/work/meeting headphones_6bb5182e-d4ea-56db-bc24-d76b7499117e.svg'
AUTHOR = 'gpt-6'


class PersonWearingHeadphones(Solo48):
    icon_id = 'person-wearing-headphones'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/work"
    aliases = ()
    keywords = ('person', 'headphones', 'audio', 'meeting', 'listener', 'headset')

    def build(self) -> None:
        self.add_arc('band', (8, 20), (40, 20), radius_x=16, radius_y=16, sweep=True, large_arc=False)
        self.add_line('cup-left', (8, 20), (8, 28))
        self.add_line('cup-right', (40, 20), (40, 28))
        self.relate("connect", 'band', 'cup-left')
        self.relate("connect", 'band', 'cup-right')
        self.add_arc('jaw', (31, 21), (17, 21), radius_x=7, radius_y=10, sweep=True, large_arc=False)
        self.add_arc('shoulder-left', (8, 42), (16, 40), radius_x=8, radius_y=4, sweep=True, large_arc=False)
        self.add_line('shoulder-top', (16, 40), (32, 40))
        self.add_arc('shoulder-right', (32, 40), (40, 42), radius_x=8, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('shoulders', 'shoulder-left', 'shoulder-top', 'shoulder-right', closed=False)
