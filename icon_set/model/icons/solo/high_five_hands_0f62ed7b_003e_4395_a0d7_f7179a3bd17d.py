"""Two raised hands meet palm to palm at the center, with their wrists spreading diagonally downward. Mirrored thumbs bend inward below the upright fingers, and three short contact rays appear above.
Lucide hand rounded finger construction. Mirrored raised palms meet at center and wrists diverge; individual fingers and thumb creases omitted. Three contact dots retained.
SQUARE: centerline extremes (6,6)-(42,42); freshly authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0f62ed7b-003e-4395-a0d7-f7179a3bd17d'
SOURCE_PATH = 'pictographic-primitives/work/workflow teamwork high five_0f62ed7b-003e-4395-a0d7-f7179a3bd17d.svg'
AUTHOR = 'gpt-6'


class HighFiveHands(Solo48):
    icon_id = 'high-five-hands'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/work"
    aliases = ()
    keywords = ('hands', 'highfive', 'greeting', 'celebration', 'contact', 'teamwork')

    def build(self) -> None:
        self.add_polyline('left-outer', (6, 42), (10, 36), (14, 20), closed=False)
        self.add_arc('left-finger', (14, 20), (24, 20), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('left-inner', (24, 30), (16, 42))
        self.relate("connect", 'left-outer', 'left-finger')
        self.add_polyline('right-outer', (42, 42), (38, 36), (34, 20), closed=False)
        self.add_arc('right-finger', (34, 20), (24, 20), radius_x=5, radius_y=5, sweep=False, large_arc=False)
        self.add_line('right-inner', (24, 30), (32, 42))
        self.relate("connect", 'right-outer', 'right-finger')
        self.add_line('contact', (24, 20), (24, 30))
        self.relate("connect", 'contact', 'left-finger')
        self.relate("connect", 'contact', 'left-inner')
        self.relate("connect", 'contact', 'right-finger')
        self.relate("connect", 'contact', 'right-inner')
        self.relate("connect", 'left-finger', 'right-finger')
        self.relate("connect", 'left-inner', 'right-inner')
        self.add_dot('ray-0', (24, 6))
        self.add_dot('ray-1', (10, 10))
        self.add_dot('ray-2', (38, 10))
