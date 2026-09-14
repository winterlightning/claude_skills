"""Two mirrored closed fists extend horizontally toward each other and meet at the center. Curled thumb lines turn inward below the contact point, with three short impact rays above.
Lucide hand rounded knuckles. Two mirrored fists meet at the center with inward thumb marks; three impact dots replace short rays. Finger creases omitted.
SQUARE: centerline extremes (6,6)-(42,42); freshly authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7eb37a5d-4cd8-4996-8500-94d9331cc88f'
SOURCE_PATH = 'pictographic-primitives/work/workflow teamwork fistbump_7eb37a5d-4cd8-4996-8500-94d9331cc88f.svg'
AUTHOR = 'gpt-6'


class FistBump(Solo48):
    icon_id = 'fist-bump'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/work"
    aliases = ()
    keywords = ('fist', 'bump', 'hands', 'greeting', 'teamwork', 'contact')

    def build(self) -> None:
        self.add_line('left-top', (6, 20), (18, 20))
        self.add_arc('left-knuckle-top', (18, 20), (24, 26), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_contour('left-upper', 'left-top', 'left-knuckle-top', closed=False)
        self.add_arc('left-knuckle-bottom', (24, 32), (18, 38), radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_polyline('left-wrist', (18, 38), (14, 42), (6, 42), closed=False)
        self.relate("connect", 'left-knuckle-bottom', 'left-wrist')
        self.add_line('left-thumb', (14, 32), (24, 32))
        self.relate("connect", 'left-thumb', 'left-knuckle-bottom')
        self.add_line('right-top', (42, 20), (30, 20))
        self.add_arc('right-knuckle-top', (30, 20), (24, 26), radius_x=6, radius_y=6, sweep=False, large_arc=False)
        self.add_contour('right-upper', 'right-top', 'right-knuckle-top', closed=False)
        self.add_arc('right-knuckle-bottom', (24, 32), (30, 38), radius_x=6, radius_y=6, sweep=False, large_arc=False)
        self.add_polyline('right-wrist', (30, 38), (34, 42), (42, 42), closed=False)
        self.relate("connect", 'right-knuckle-bottom', 'right-wrist')
        self.add_line('right-thumb', (34, 32), (24, 32))
        self.relate("connect", 'right-thumb', 'right-knuckle-bottom')
        self.add_line('contact', (24, 26), (24, 32))
        self.relate("connect", 'contact', 'left-upper')
        self.relate("connect", 'contact', 'left-knuckle-bottom')
        self.relate("connect", 'contact', 'left-thumb')
        self.relate("connect", 'contact', 'right-upper')
        self.relate("connect", 'contact', 'right-knuckle-bottom')
        self.relate("connect", 'contact', 'right-thumb')
        self.relate("connect", 'left-upper', 'right-upper')
        self.relate("connect", 'left-knuckle-bottom', 'right-knuckle-bottom')
        self.relate("connect", 'left-thumb', 'right-thumb')
        self.relate("connect", 'left-thumb', 'right-knuckle-bottom')
        self.relate("connect", 'right-thumb', 'left-knuckle-bottom')
        self.add_dot('ray-top', (24, 6))
        self.add_dot('ray-left', (14, 10))
        self.add_dot('ray-right', (34, 10))
