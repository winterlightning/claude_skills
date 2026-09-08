"""Bee with stripes and paired rounded wings; centerline extremes (2,2)-(46,46). Lucide bug informs body arcs and paired appendages. Antennae meet at crown to preserve clear space."""
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
        # Bee with stripes and paired rounded wings; centerline extremes (2,2)-(46,46). Lucide bug informs body arcs and paired appendages. Antennae meet at crown to preserve clear space.
        self.add_arc('head-left', (15, 19), (24, 8), radius_x=9, radius_y=11, sweep=True)
        self.add_arc('head-right', (24, 8), (33, 19), radius_x=9, radius_y=11, sweep=True)
        self.add_line('side-right-top', (33, 19), (33, 23))
        self.add_line('side-right-mid', (33, 23), (33, 32))
        self.add_line('side-right-low', (33, 32), (33, 35))
        self.add_arc('abdomen-right', (33, 35), (24, 44), radius_x=9, radius_y=9, sweep=True)
        self.add_arc('abdomen-left', (24, 44), (15, 35), radius_x=9, radius_y=9, sweep=True)
        self.add_line('side-left-low', (15, 35), (15, 32))
        self.add_line('side-left-mid', (15, 32), (15, 23))
        self.add_line('side-left-top', (15, 23), (15, 19))
        self.add_contour('body', 'head-left', 'head-right', 'side-right-top', 'side-right-mid', 'side-right-low', 'abdomen-right', 'abdomen-left', 'side-left-low', 'side-left-mid', 'side-left-top', closed=True)
        self.add_line('stripe-top', (15, 23), (33, 23))
        self.relate("connect", 'stripe-top', 'body')
        self.add_line('stripe-bottom', (15, 32), (33, 32))
        self.relate("connect", 'stripe-bottom', 'body')
        self.add_line('left-antenna', (17, 2), (24, 8))
        self.relate("connect", 'left-antenna', 'body')
        self.add_line('right-antenna', (31, 2), (24, 8))
        self.relate("connect", 'right-antenna', 'body')
        self.relate("connect", 'left-antenna', 'right-antenna')
        self.add_line('stinger', (24, 44), (24, 46))
        self.relate("connect", 'stinger', 'body')
        self.add_line('left-wing-top', (15, 19), (4, 27))
        self.add_arc('left-wing-round-top', (4, 27), (2, 32), radius_x=2, radius_y=5, sweep=False)
        self.add_arc('left-wing-round-bottom', (2, 32), (9, 39), radius_x=7, radius_y=7, sweep=False)
        self.add_arc('left-wing-return', (9, 39), (15, 35), radius_x=6, radius_y=4, sweep=False)
        self.add_contour('left-wing', 'left-wing-top', 'left-wing-round-top', 'left-wing-round-bottom', 'left-wing-return', closed=False)
        self.relate("connect", 'left-wing', 'body')
        self.add_line('right-wing-top', (33, 19), (44, 27))
        self.add_arc('right-wing-round-top', (44, 27), (46, 32), radius_x=2, radius_y=5, sweep=True)
        self.add_arc('right-wing-round-bottom', (46, 32), (39, 39), radius_x=7, radius_y=7, sweep=True)
        self.add_arc('right-wing-return', (39, 39), (33, 35), radius_x=6, radius_y=4, sweep=True)
        self.add_contour('right-wing', 'right-wing-top', 'right-wing-round-top', 'right-wing-round-bottom', 'right-wing-return', closed=False)
        self.relate("connect", 'right-wing', 'body')
