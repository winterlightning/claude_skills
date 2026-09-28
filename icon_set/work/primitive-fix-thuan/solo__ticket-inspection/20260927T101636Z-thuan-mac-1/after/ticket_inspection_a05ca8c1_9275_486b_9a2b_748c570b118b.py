"Two standing people face forward beside one another. The left figure raises a small rectangular ticket between their heads, while the right figure extends an arm toward the other person's waist.\n\nConstruction: Two waist-up people hold a clearly separated ticket between them. Individual legs are omitted; the radial keyshape accommodates the diagonal figure extremes without crowding the paper. Centerline radius20.\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used."
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'a05ca8c1-9275-486b-9a2b-748c570b118b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__ticket-inspection/20260927T101636Z-thuan-mac-1/reference/information desk ticket_a05ca8c1-9275-486b-9a2b-748c570b118b.svg'
AUTHOR = 'gpt-6'

class TicketInspection(Solo48):
    icon_id = 'ticket-inspection'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('ticket', 'inspection', 'people', 'admission', 'service', 'pass')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('inspector-head-top', (7, 15), (13, 15), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('inspector-head-bottom', (13, 15), (7, 15), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_bezier('inspector-body-1',(10,27),((8,29),(8,34),(10,38)))
        self.add_line('inspector-arm-1', (10, 27), (20, 24))
        self.add_arc('passenger-head-top', (35, 15), (41, 15), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('passenger-head-bottom', (41, 15), (35, 15), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_bezier('passenger-body-1',(38,27),((40,29),(40,34),(38,38)))
        self.add_line('passenger-arm-1', (38, 27), (28, 24))
        self.add_line('ticket-1', (20, 24), (28, 24))
        self.add_line('ticket-2', (28, 24), (28, 32))
        self.add_line('ticket-3', (28, 32), (20, 32))
        self.add_line('ticket-4', (20, 32), (20, 24))
        self.add_contour('inspector-head', 'inspector-head-top', 'inspector-head-bottom', closed=True)
        self.add_contour('inspector-body', 'inspector-body-1', closed=False)
        self.add_contour('inspector-arm', 'inspector-arm-1', closed=False)
        self.add_contour('passenger-head', 'passenger-head-top', 'passenger-head-bottom', closed=True)
        self.add_contour('passenger-body', 'passenger-body-1', closed=False)
        self.add_contour('passenger-arm', 'passenger-arm-1', closed=False)
        self.add_contour('ticket', 'ticket-1', 'ticket-2', 'ticket-3', 'ticket-4', closed=True)
        self.relate('connect', 'inspector-body', 'inspector-arm')
        self.relate('connect', 'passenger-body', 'passenger-arm')
        self.relate('connect', 'ticket', 'inspector-arm')
        self.relate('connect', 'ticket', 'passenger-arm')
