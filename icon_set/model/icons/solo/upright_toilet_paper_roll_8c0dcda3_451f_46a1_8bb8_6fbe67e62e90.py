'A toilet paper roll stands upright as a cylinder with an elliptical top and small central opening. A loose sheet extends rightward with an irregular zigzag torn edge.\n\nConstruction: Upright roll with elliptical top and a loose paper tail at the right. Bounds (4,8)-(44,40).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8c0dcda3-451f-46a1-8bb8-6fbe67e62e90'
SOURCE_PATH = 'pictographic-primitives/wayfinding/toilet paper 1_8c0dcda3-451f-46a1-8bb8-6fbe67e62e90.svg'
AUTHOR = 'gpt-6'

class UprightToiletPaperRoll(Solo48):
    icon_id = 'upright-toilet-paper-roll'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('toilet', 'paper', 'roll', 'tissue', 'bathroom', 'hygiene')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('top-front', (4, 14), (32, 14), radius_x=14, radius_y=6, large_arc=False, sweep=False)
        self.add_arc('top-back', (32, 14), (4, 14), radius_x=14, radius_y=6, large_arc=False, sweep=False)
        self.add_line('left-side', (4, 14), (4, 34))
        self.add_arc('base', (4, 34), (32, 34), radius_x=14, radius_y=6, large_arc=False, sweep=False)
        self.add_line('right-side-joint-1', (32, 34), (32, 18))
        self.add_line('right-side-joint-2', (32, 18), (32, 14))
        self.add_line('tail-1', (32, 18), (44, 18))
        self.add_line('tail-2', (44, 18), (40, 28))
        self.add_line('tail-3', (40, 28), (44, 38))
        self.add_line('tail-4', (44, 38), (32, 38))
        self.add_contour('top', 'top-front', 'top-back', closed=True)
        self.add_contour('roll', 'left-side', 'base', 'right-side-joint-1', 'right-side-joint-2', closed=False)
        self.add_contour('tail', 'tail-1', 'tail-2', 'tail-3', 'tail-4', closed=False)
        self.relate('connect', 'roll', 'top')
        self.relate('connect', 'tail', 'roll')
