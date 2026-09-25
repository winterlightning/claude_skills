'Four diagonal arrows point inward toward a small central circle. The arrows occupy the four corners in a balanced arrangement, leaving a clear gap around the centre.\n\nConstruction: Four mirrored corner arrows converge on a small circle. Bounds (6,6)-(42,42).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '85e727bb-b42f-4e94-8d63-48f14ffcd7a5'
SOURCE_PATH = 'pictographic-primitives/wayfinding/meeting point_85e727bb-b42f-4e94-8d63-48f14ffcd7a5.svg'
AUTHOR = 'gpt-6'

class MeetingPointSymbol(Solo48):
    icon_id = 'meeting-point-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('meeting', 'assembly', 'point', 'arrows', 'gathering', 'wayfinding')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('center-top', (21, 24), (27, 24), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('center-bottom', (27, 24), (21, 24), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('shaft-0', (6, 6), (15, 15))
        self.add_line('head-0-1', (8, 15), (15, 15))
        self.add_line('head-0-2', (15, 15), (15, 8))
        self.add_line('shaft-1', (42, 6), (33, 15))
        self.add_line('head-1-1', (40, 15), (33, 15))
        self.add_line('head-1-2', (33, 15), (33, 8))
        self.add_line('shaft-2', (6, 42), (15, 33))
        self.add_line('head-2-1', (8, 33), (15, 33))
        self.add_line('head-2-2', (15, 33), (15, 40))
        self.add_line('shaft-3', (42, 42), (33, 33))
        self.add_line('head-3-1', (40, 33), (33, 33))
        self.add_line('head-3-2', (33, 33), (33, 40))
        self.add_contour('center', 'center-top', 'center-bottom', closed=True)
        self.add_contour('head-0', 'head-0-1', 'head-0-2', closed=False)
        self.add_contour('head-1', 'head-1-1', 'head-1-2', closed=False)
        self.add_contour('head-2', 'head-2-1', 'head-2-2', closed=False)
        self.add_contour('head-3', 'head-3-1', 'head-3-2', closed=False)
        self.relate('connect', 'shaft-0', 'head-0')
        self.relate('connect', 'shaft-1', 'head-1')
        self.relate('connect', 'shaft-2', 'head-2')
        self.relate('connect', 'shaft-3', 'head-3')
