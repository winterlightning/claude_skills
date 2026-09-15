"""A standing person faces left and reaches across a desk toward a slanted writing implement. Two horizontal document lines sit above the left side of the desk, beside the worker's upright body.
Lucide user circular head and laptop side construction. Source-facing direction is deliberate; doubled limbs and chair pedestal omitted, seated knee or standing leg retained. Writing lines reduced to one.
Keyshape SQUARE; centerline extremes (6,6)-(42,42). Square envelope balances the complete scene. Source inspected as a standalone physical or conceptual subject."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6b40dc1d-d719-46f6-87c3-95cd2d0dd7ee'
SOURCE_PATH = 'pictographic-primitives/work/desk document base work standing user_6b40dc1d-d719-46f6-87c3-95cd2d0dd7ee.svg'
AUTHOR = 'gpt-6'


class StandingPersonWritingAtDesk(Solo48):
    icon_id = 'standing-person-writing-at-desk'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/work"
    aliases = ()
    keywords = ('person', 'writing', 'standing', 'desk', 'document', 'office')

    def build(self) -> None:
        self.add_arc('head-top', (32, 10), (40, 10), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('head-bottom', (40, 10), (32, 10), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_polyline('body', (36, 23), (36, 33), (36, 42), closed=False)
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
        self.add_line('foot', (36, 42), (42, 42))
        self.relate("connect", 'foot', 'body')
