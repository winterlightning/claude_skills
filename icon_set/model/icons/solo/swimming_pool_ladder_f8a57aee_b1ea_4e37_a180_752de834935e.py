'Two tall curved handrails form a pool ladder with three horizontal rungs between them. The lower ends disappear behind two gently scalloped rows of water.\n\nConstruction: Two matching hooked rails and one rung above water. Bounds (4,8)-(44,40).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f8a57aee-b1ea-4e37-a180-752de834935e'
SOURCE_PATH = 'pictographic-primitives/wayfinding/swimming pool stairs_f8a57aee-b1ea-4e37-a180-752de834935e.svg'
AUTHOR = 'gpt-6'

class SwimmingPoolLadder(Solo48):
    icon_id = 'swimming-pool-ladder'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    aliases = ()
    keywords = ('pool', 'ladder', 'swimming', 'water', 'rungs', 'handrail')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('hook-9', (21, 14), (9, 14), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_line('rail-9-joint-1', (9, 14), (9, 23))
        self.add_line('rail-9-joint-2', (9, 23), (9, 27))
        self.add_arc('hook-30', (42, 14), (30, 14), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_line('rail-30-joint-1', (30, 14), (30, 23))
        self.add_line('rail-30-joint-2', (30, 23), (30, 27))
        self.add_line('rung', (9, 23), (30, 23))
        self.add_arc('water-0', (4, 38), (14, 38), radius_x=5, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('water-1', (14, 38), (24, 38), radius_x=5, radius_y=2, large_arc=False, sweep=False)
        self.add_arc('water-2', (24, 38), (34, 38), radius_x=5, radius_y=2, large_arc=False, sweep=True)
        self.add_arc('water-3', (34, 38), (44, 38), radius_x=5, radius_y=2, large_arc=False, sweep=False)
        self.add_contour('rail-group-9', 'hook-9', 'rail-9-joint-1', 'rail-9-joint-2', closed=False)
        self.add_contour('rail-group-30', 'hook-30', 'rail-30-joint-1', 'rail-30-joint-2', closed=False)
        self.add_contour('water', 'water-0', 'water-1', 'water-2', 'water-3', closed=False)
        self.relate('connect', 'rung', 'rail-group-9')
        self.relate('connect', 'rung', 'rail-group-30')
