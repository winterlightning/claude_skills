"""A person sits in a pedestal chair facing left toward a monitor on a desk. A curved support joins the tilted monitor to the desktop, while the worker reaches forward above bent legs.
Lucide user circular head and laptop side construction. Source-facing direction is deliberate; doubled limbs and chair pedestal omitted, seated knee or standing leg retained. Writing lines reduced to one.
Keyshape SQUARE; centerline extremes (6,6)-(42,42). Square envelope balances the complete scene. Source inspected as a standalone physical or conceptual subject."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c1715918-c18f-56f9-9588-99c5e5e7592e'
SOURCE_PATH = 'pictographic-primitives/work/desk computer base work sitting user_c1715918-c18f-56f9-9588-99c5e5e7592e.svg'
AUTHOR = 'gpt-6'


class SeatedDesktopComputerWorker(Solo48):
    icon_id = 'seated-desktop-computer-worker'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "work"
    aliases = ()
    keywords = ('worker', 'computer', 'monitor', 'desk', 'chair', 'office')

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
        self.add_line('screen', (6, 6), (10, 17))
        self.add_polyline('monitor-support', (10, 17), (14, 21), (14, 25), closed=False)
        self.relate("connect", 'screen', 'monitor-support')
        self.relate("connect", 'monitor-support', 'desktop')
        self.relate("connect", 'monitor-support', 'desk-leg')
        self.add_line('seat', (36, 33), (42, 33))
        self.relate("connect", 'seat', 'body')
        self.relate("connect", 'seat', 'arm')
