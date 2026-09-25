'An irregular cliff edge slopes down toward the right and meets a flat baseline. Three separate angular rocks descend through the open space beside the cliff face.\n\nConstruction: Broken cliff silhouette beside two falling rocks; angular fragments retain the hazard subject. Bounds (6,6)-(42,42).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c6e6f4ad-3d18-5e8f-b980-35b1518b0073'
SOURCE_PATH = 'pictographic-primitives/wayfinding/safety danger mudslide_c6e6f4ad-3d18-5e8f-b980-35b1518b0073.svg'
AUTHOR = 'gpt-6'

class FallingRocks(Solo48):
    icon_id = 'falling-rocks'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    aliases = ()
    keywords = ('rocks', 'falling', 'cliff', 'landslide', 'hazard', 'safety')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_line('cliff-1', (6, 6), (12, 10))
        self.add_line('cliff-2', (12, 10), (14, 20))
        self.add_line('cliff-3', (14, 20), (24, 30))
        self.add_line('cliff-4', (24, 30), (28, 42))
        self.add_line('cliff-5', (28, 42), (6, 42))
        self.add_line('rock-high-1', (30, 10), (38, 6))
        self.add_line('rock-high-2', (38, 6), (42, 14))
        self.add_line('rock-high-3', (42, 14), (34, 18))
        self.add_line('rock-high-4', (34, 18), (30, 10))
        self.add_arc('rock-low-top', (36, 35), (42, 35), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('rock-low-bottom', (42, 35), (36, 35), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('cliff', 'cliff-1', 'cliff-2', 'cliff-3', 'cliff-4', 'cliff-5', closed=False)
        self.add_contour('rock-high', 'rock-high-1', 'rock-high-2', 'rock-high-3', 'rock-high-4', closed=True)
        self.add_contour('rock-low', 'rock-low-top', 'rock-low-bottom', closed=True)
