'A rectangular fire alarm panel carries the word FIRE above an inset push area. Two inward-pointing arrows flank a central circular button within the lower rectangular recess.\n\nConstruction: An emergency panel with a large central flame cue. The source text, arrows, inset frame and button cannot coexist with SOLO48 spacing and are represented by the flame. Bounds (6,6)-(42,42).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'e165b9e1-c8b5-484a-bb6a-7bd58893013f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__manual-fire-alarm-call-point/20260927T032104Z-thuan-mac-1/reference/safety fire_e165b9e1-c8b5-484a-bb6a-7bd58893013f.svg'
AUTHOR = "gpt-6"

class ManualFireAlarmCallPoint(Solo48):
    icon_id = 'manual-fire-alarm-call-point'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('fire', 'alarm', 'button', 'panel', 'emergency', 'safety')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_line('panel-0', (10, 6), (38, 6))
        self.add_arc('panel-1', (38, 6), (42, 10), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('panel-2', (42, 10), (42, 38))
        self.add_arc('panel-3', (42, 38), (38, 42), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('panel-4', (38, 42), (10, 42))
        self.add_arc('panel-5', (10, 42), (6, 38), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('panel-6', (6, 38), (6, 10))
        self.add_arc('panel-7', (6, 10), (10, 6), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        # A single flame fills the action zone with a clear fire cue.
        self.add_polyline('flame',
            (24, 15), (30, 23), (30, 29), (27, 33),
            (21, 33), (18, 29), (18, 23), (24, 15), closed=True)
        self.add_contour('panel', 'panel-0', 'panel-1', 'panel-2', 'panel-3', 'panel-4', 'panel-5', 'panel-6', 'panel-7', closed=True)
