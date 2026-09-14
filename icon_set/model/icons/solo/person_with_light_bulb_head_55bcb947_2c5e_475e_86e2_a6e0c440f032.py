"""A glowing light bulb replaces the head above a broad suited bust. A pointed collar and central tie sit beneath the bulb's base, with short rays around the rounded glass.
Lucide lightbulb and user shoulder arcs. Bulb replaces the head; intrinsic conceptual portrait. Tie and diagonal rays removed for clarity.
Keyshape SQUARE; centerline extremes (6,6)-(42,42). Square envelope balances the complete scene. Source inspected as a standalone physical or conceptual subject."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '55bcb947-2c5e-475e-86e2-a6e0c440f032'
SOURCE_PATH = 'pictographic-primitives/work/head idea_55bcb947-2c5e-475e-86e2-a6e0c440f032.svg'
AUTHOR = 'gpt-6'


class PersonWithLightBulbHead(Solo48):
    icon_id = 'person-with-light-bulb-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/work"
    aliases = ()
    keywords = ('person', 'bulb', 'idea', 'creativity', 'suit', 'thinking')

    def build(self) -> None:
        self.add_arc('glass-top', (16, 23), (32, 23), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('glass-right', (32, 23), (29, 29), radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_line('base', (29, 29), (19, 29))
        self.add_arc('glass-left', (19, 29), (16, 23), radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_contour('glass', 'glass-top', 'glass-right', 'base', 'glass-left', closed=True)
        self.add_dot('ray-top', (24, 6))
        self.add_line('ray-left', (6, 22), (7, 22))
        self.add_line('ray-right', (41, 22), (42, 22))
        self.add_arc('shoulder-left', (6, 42), (18, 38), radius_x=12, radius_y=4, sweep=True, large_arc=False)
        self.add_line('collar-left', (18, 38), (24, 42))
        self.add_line('collar-right', (24, 42), (30, 38))
        self.add_arc('shoulder-right', (30, 38), (42, 42), radius_x=12, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('bust', 'shoulder-left', 'collar-left', 'collar-right', 'shoulder-right', closed=False)
