"""A person sits on a pedestal office chair facing left toward a laptop on a desk. Both arms extend toward the desktop, and the bent legs project forward beneath it.
Lucide user circular head and laptop side construction. Source-facing direction is deliberate; doubled limbs and chair pedestal omitted, seated knee or standing leg retained. Writing lines reduced to one.
Keyshape SQUARE; centerline extremes (6,6)-(42,42). Square envelope balances the complete scene. Source inspected as a standalone physical or conceptual subject."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4b08589f-758f-4ceb-88c8-6fb2b68847fc'
SOURCE_PATH = 'pictographic-primitives/work/desk computer base work laptop sitting user_4b08589f-758f-4ceb-88c8-6fb2b68847fc.svg'
AUTHOR = 'gpt-6'

class SeatedLaptopWorkerVariant2(Solo48):
    icon_id = 'seated-laptop-worker-v2'
    variant_of = 'seated-laptop-worker'
    variant_label = 'Hole and centerline reconstruction'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/work'
    aliases = ()
    keywords = ('worker', 'laptop', 'desk', 'chair', 'office', 'seated')

    def build(self) -> None:
        """Keep the desk edge once, split its true laptop and leg attachments, and set the head-to-shoulder ink gap to4."""
        self.add_arc('head-top', (32, 10), (40, 10), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('head-bottom', (40, 10), (32, 10), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_polyline('body', (36, 22), (36, 33), (26, 33), (22, 42), closed=False)
        self.add_polyline('arm', (36, 22), (28, 25), (24, 25), closed=False)
        self.relate('connect', 'arm', 'body')
        self.add_polyline('desktop', (6, 25), (8, 25), (11, 25), (24, 25))
        self.relate('connect', 'desktop', 'arm')
        self.add_line('desk-leg', (8, 25), (8, 42))
        self.relate('connect', 'desk-leg', 'desktop')
        self.add_line('laptop', (6, 10), (11, 25))
        self.relate('connect', 'laptop', 'desktop')
        self.relate('connect', 'laptop', 'desk-leg')
        self.add_line('seat', (36, 33), (42, 33))
        self.relate('connect', 'seat', 'body')
        self.relate('connect', 'seat', 'arm')
