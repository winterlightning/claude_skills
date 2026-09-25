"""A seated person faces left with an arm reaching across a desk toward an angled writing implement. Three horizontal document lines float above the desk; a pedestal chair supports the bent figure.
Lucide user circular head and laptop side construction. Source-facing direction is deliberate; doubled limbs and chair pedestal omitted, seated knee or standing leg retained. Writing lines reduced to one.
Keyshape SQUARE; centerline extremes (6,6)-(42,42). Square envelope balances the complete scene. Source inspected as a standalone physical or conceptual subject."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c70f0528-e534-53ea-99dd-1c170698167d'
SOURCE_PATH = 'pictographic-primitives/work/desk document base work sitting user_c70f0528-e534-53ea-99dd-1c170698167d.svg'
AUTHOR = 'gpt-6'


class SeatedPersonWritingAtDesk(Solo48):
    icon_id = 'seated-person-writing-at-desk'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "work"
    aliases = ()
    keywords = ('person', 'writing', 'desk', 'document', 'seated', 'office')

    def build(self) -> None:
        self.add_arc('head-top', (32, 10), (40, 10), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('head-bottom', (40, 10), (32, 10), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_polyline('body', (36, 23), (36, 33), (26, 33), (22, 42), closed=False)
        self.add_polyline('arm', (36, 23), (28, 25), (24, 25), closed=False)
        self.relate("connect", 'arm', 'body')
        self.add_line('desktop', (6, 25), (24, 25))
        self.relate("connect", 'desktop', 'arm')
        self.add_line('desk-leg', (8, 25), (8, 42))
        self.relate("connect", 'desk-leg', 'desktop')
        self.add_line('pen', (17, 15), (12, 25))
        self.relate("connect", 'pen', 'desktop')
        self.relate("connect", 'pen', 'desk-leg')
        self.add_line('document', (6, 6), (19, 6))
        self.add_line('seat', (36, 33), (42, 33))
        self.relate("connect", 'seat', 'body')
        self.relate("connect", 'seat', 'arm')
