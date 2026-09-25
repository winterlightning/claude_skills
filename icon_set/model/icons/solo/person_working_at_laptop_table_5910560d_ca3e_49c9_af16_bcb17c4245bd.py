"""A seated person faces right toward an open laptop on a small table. The circular head sits above a bent torso, forward-reaching arm and bent legs; two splayed legs support the table.
Lucide user circular head and laptop side construction. Source-facing direction is deliberate; doubled limbs and chair pedestal omitted, seated knee or standing leg retained. Writing lines reduced to one.
Keyshape SQUARE; centerline extremes (6,6)-(42,42). Square envelope balances the complete scene. Source inspected as a standalone physical or conceptual subject."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5910560d-ca3e-49c9-af16-bcb17c4245bd'
SOURCE_PATH = 'pictographic-primitives/work/co working space laptop_5910560d-ca3e-49c9-af16-bcb17c4245bd.svg'
AUTHOR = 'gpt-6'

class PersonWorkingAtLaptopTable(Solo48):
    icon_id = 'person-working-at-laptop-table'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'work'
    categories = ('work', 'primitives')
    aliases = ()
    keywords = ('person', 'laptop', 'desk', 'work', 'seated', 'computer')

    def build(self) -> None:
        """Keep the desk edge once, split its true laptop and leg attachments, and set the head-to-shoulder ink gap to4."""
        self.add_arc('head-top', (8, 10), (16, 10), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('head-bottom', (16, 10), (8, 10), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_polyline('body', (12, 22), (12, 33), (22, 33), (26, 42), closed=False)
        self.add_polyline('arm', (12, 22), (20, 25), (24, 25), closed=False)
        self.relate('connect', 'arm', 'body')
        self.add_polyline('desktop', (42, 25), (40, 25), (37, 25), (24, 25))
        self.relate('connect', 'desktop', 'arm')
        self.add_line('desk-leg', (40, 25), (40, 42))
        self.relate('connect', 'desk-leg', 'desktop')
        self.add_line('laptop', (42, 10), (37, 25))
        self.relate('connect', 'laptop', 'desktop')
        self.relate('connect', 'laptop', 'desk-leg')
        self.add_line('seat', (12, 33), (6, 33))
        self.relate('connect', 'seat', 'body')
        self.relate('connect', 'seat', 'arm')
