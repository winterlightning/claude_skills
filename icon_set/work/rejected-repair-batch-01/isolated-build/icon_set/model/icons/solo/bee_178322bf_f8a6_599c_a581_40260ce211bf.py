"""Bee with stripes and paired rounded wings; centerline extremes (6,6)-(42,42). Lucide bug informs body arcs and paired appendages. Antennae meet at crown to preserve clear space."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '178322bf-f8a6-599c-a581-40260ce211bf'
SOURCE_PATH = 'pictographic-primitives/animals/bee_178322bf-f8a6-599c-a581-40260ce211bf.svg'
AUTHOR = 'gpt-6'


class HoneyBee(Solo48):
    icon_id = 'honey-bee'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('bee', 'honeybee', 'insect', 'wings', 'stripes', 'honey', 'pollinate', 'bug')

    def build(self) -> None:
        # Bee with stripes and paired rounded wings; centerline extremes (6,6)-(42,42). Lucide bug informs body arcs and paired appendages. Antennae meet at crown to preserve clear space.
        self.add_arc('head-left', (15, 19), (24, 8), radius_x=9, radius_y=11, sweep=True)
        self.add_arc('head-right', (24, 8), (33, 19), radius_x=9, radius_y=11, sweep=True)
        self.add_line('side-right-top', (33, 19), (33, 23))
        self.add_line('side-right-mid', (33, 23), (33, 32))
        self.add_line('side-right-low', (33, 32), (33, 35))
        self.add_bezier('abdomen-right', (33, 35), *(((32.04905494, 39.17840292), (28.28391546, 42), (24, 42)),))
        self.add_bezier('abdomen-left', (24, 42), *(((19.71608454, 42), (15.95094506, 39.17840292), (15, 35)),))
        self.add_line('side-left-low', (15, 35), (15, 32))
        self.add_line('side-left-mid', (15, 32), (15, 23))
        self.add_line('side-left-top', (15, 23), (15, 19))
        self.add_contour('body', 'head-left', 'head-right', 'side-right-top', 'side-right-mid', 'side-right-low', 'abdomen-right', 'abdomen-left', 'side-left-low', 'side-left-mid', 'side-left-top', closed=True)
        self.add_line('stripe-top', (15, 23), (33, 23))
        self.relate("connect", 'stripe-top', 'body')
        self.add_line('stripe-bottom', (15, 32), (33, 32))
        self.relate("connect", 'stripe-bottom', 'body')
        self.add_line('left-antenna', (17, 6), (24, 8))
        self.relate("connect", 'left-antenna', 'body')
        self.add_line('right-antenna', (31, 6), (24, 8))
        self.relate("connect", 'right-antenna', 'body')
        self.relate("connect", 'left-antenna', 'right-antenna')
        self.add_line('stinger', (24, 42), (24, 42))
        self.relate("connect", 'stinger', 'body')
        self.add_line('left-wing-top', (15, 19), (6, 27))
        self.add_bezier('left-wing-round-top', (6, 27), *(((6, 28.54700538), (6, 30.45299462), (6, 32)),))
        self.add_bezier('left-wing-round-bottom', (6, 32), *(((6, 34.72076519), (6.70714356, 37.46238974), (9, 39)),))
        self.add_arc('left-wing-return', (9, 39), (15, 35), radius_x=6, radius_y=4, sweep=False)
        self.add_contour('left-wing', 'left-wing-top', 'left-wing-round-top', 'left-wing-round-bottom', 'left-wing-return', closed=False)
        self.relate("connect", 'left-wing', 'body')
        self.add_line('right-wing-top', (33, 19), (42, 27))
        self.add_bezier('right-wing-round-top', (42, 27), *(((42, 28.54700538), (42, 30.45299462), (42, 32)),))
        self.add_bezier('right-wing-round-bottom', (42, 32), *(((42, 34.72076519), (41.29285644, 37.46238974), (39, 39)),))
        self.add_arc('right-wing-return', (39, 39), (33, 35), radius_x=6, radius_y=4, sweep=True)
        self.add_contour('right-wing', 'right-wing-top', 'right-wing-round-top', 'right-wing-round-bottom', 'right-wing-return', closed=False)
        self.relate("connect", 'right-wing', 'body')
