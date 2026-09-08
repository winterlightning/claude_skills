"""Open spiral snake with a broad right-hand head; eye dots omitted to preserve space. Centerline extremes (5,2)-(43,46), natural asymmetric coil."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bd9f57fc-780e-5c9d-8047-c776f0b4d870'
SOURCE_PATH = 'pictographic-primitives/animals/reptile snake_bd9f57fc-780e-5c9d-8047-c776f0b4d870.svg'
AUTHOR = 'gpt-6'


class CoiledSnake(Solo48):
    icon_id = 'coiled-snake'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('snake', 'coil', 'spiral', 'serpent', 'reptile', 'curl', 'python', 'wild')

    def build(self) -> None:
        self.add_arc('snake-1', (18, 38), (5, 21), radius_x=19, radius_y=19, sweep=True)
        self.add_arc('snake-2', (5, 21), (24, 2), radius_x=19, radius_y=19, sweep=True)
        self.add_arc('snake-3', (24, 2), (43, 21), radius_x=19, radius_y=19, sweep=True)
        self.add_line('snake-4', (43, 21), (43, 29))
        self.add_line('snake-5', (43, 29), (40, 40))
        self.add_arc('snake-6', (40, 40), (34, 46), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('snake-7', (34, 46), (28, 40), radius_x=6, radius_y=6, sweep=True)
        self.add_line('snake-8', (28, 40), (26, 29))
        self.add_arc('snake-9', (26, 29), (30, 23), radius_x=8, radius_y=8, sweep=True)
        self.add_arc('snake-10', (30, 23), (24, 12), radius_x=8, radius_y=11, sweep=False)
        self.add_arc('snake-11', (24, 12), (13, 23), radius_x=11, radius_y=11, sweep=False)
        self.add_arc('snake-12', (13, 23), (24, 34), radius_x=11, radius_y=11, sweep=False)
        self.add_arc('snake-13', (24, 34), (18, 38), radius_x=8, radius_y=8, sweep=True)
        self.add_contour('snake', 'snake-1', 'snake-2', 'snake-3', 'snake-4', 'snake-5', 'snake-6', 'snake-7', 'snake-8', 'snake-9', 'snake-10', 'snake-11', 'snake-12', 'snake-13', closed=True)
