'Two people face each other across a narrow counter. The left person raises a rectangular sheet between them, while the right person rests a bent arm on the counter top.\n\nConstruction: Two waist-up people present a sheet across a small counter. Legs of the people are omitted; the sheet rests on the counter supports. Radial centerline envelope radius20 accommodates the figure extremes.\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7af18c91-7234-4e18-a080-60a80cd71587'
SOURCE_PATH = 'pictographic-primitives/wayfinding/information desk paper_7af18c91-7234-4e18-a080-60a80cd71587.svg'
AUTHOR = 'gpt-6'

class PersonPresentingPaperAtCounter(Solo48):
    icon_id = 'person-presenting-paper-at-counter'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('counter', 'paper', 'person', 'service', 'desk', 'document')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('customer-head-top', (7, 15), (13, 15), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('customer-head-bottom', (13, 15), (7, 15), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('customer-body-1', (10, 27), (10, 38))
        self.add_line('customer-arm-1', (10, 27), (18, 25))
        self.add_arc('attendant-head-top', (35, 15), (41, 15), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('attendant-head-bottom', (41, 15), (35, 15), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('attendant-body-1', (38, 27), (38, 38))
        self.add_line('attendant-arm-1', (38, 27), (30, 25))
        self.add_line('paper-1', (18, 25), (30, 25))
        self.add_line('paper-2', (30, 25), (30, 37))
        self.add_line('paper-3', (30, 37), (18, 37))
        self.add_line('paper-4', (18, 37), (18, 25))
        self.add_line('counter-left', (18, 37), (18, 42))
        self.add_line('counter-right', (30, 37), (30, 42))
        self.add_contour('customer-head', 'customer-head-top', 'customer-head-bottom', closed=True)
        self.add_contour('customer-body', 'customer-body-1', closed=False)
        self.add_contour('customer-arm', 'customer-arm-1', closed=False)
        self.add_contour('attendant-head', 'attendant-head-top', 'attendant-head-bottom', closed=True)
        self.add_contour('attendant-body', 'attendant-body-1', closed=False)
        self.add_contour('attendant-arm', 'attendant-arm-1', closed=False)
        self.add_contour('paper', 'paper-1', 'paper-2', 'paper-3', 'paper-4', closed=True)
        self.relate('connect', 'customer-body', 'customer-arm')
        self.relate('connect', 'attendant-body', 'attendant-arm')
        self.relate('connect', 'paper', 'customer-arm')
        self.relate('connect', 'paper', 'attendant-arm')
        self.relate('connect', 'counter-left', 'paper')
        self.relate('connect', 'counter-right', 'paper')
