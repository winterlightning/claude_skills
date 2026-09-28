"""Diagonal paintbrush with curved handle, distinct wide ferrule and a soft bristle tip. Shared diagonal attachment nodes keep the three parts coherent."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "1abc0ab3-cc14-5329-b46e-3658f7db2237"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__paintbrush-with-separate-ferrule-solo-b017/20260926T093246Z-thuan-mac/reference/brush_1abc0ab3-cc14-5329-b46e-3658f7db2237.svg"
AUTHOR = "claude-opus-5-5"

class Drawing(Solo48):
    icon_id='paintbrush-with-separate-ferrule-solo-b017'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("other", "primitives-generate")
    aliases=()
    keywords=()

    def build(self):
        # Symbol plan (SQUARE 6..42): brush on the 45-degree axis from the top
        # right to the bristle tip at (6,42).
        # Handle: straight tube, sides on x+y=41 and x+y=55 (~9.9 wide), r5 round
        # end centred (37,11) (3-4-5 end points) touching the top and right edges.
        # Ferrule: wider band between x-y=11 and x-y=-1, 15.6 across, the handle
        # sides landing on its top edge. Bristles: two cubics from the ferrule
        # corners converging to the pointed tip.
        L = self.add_line
        join = lambda a, b: self.relate('connect', a, b)
        L('handle-left', (26, 15), (34, 7))
        self.add_arc('handle-end', (34, 7), (41, 14), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        L('handle-right', (41, 14), (33, 22))
        self.add_contour('handle', 'handle-left', 'handle-end', 'handle-right')
        L('ferrule-t1', (24, 13), (26, 15)); L('ferrule-t2', (26, 15), (33, 22)); L('ferrule-t3', (33, 22), (35, 24))
        L('ferrule-r', (35, 24), (29, 30)); L('ferrule-b', (29, 30), (18, 19)); L('ferrule-l', (18, 19), (24, 13))
        self.add_contour('ferrule', 'ferrule-t1', 'ferrule-t2', 'ferrule-t3', 'ferrule-r', 'ferrule-b', 'ferrule-l', closed=True)
        join('handle', 'ferrule')
        self.add_bezier('bristle-left', (18, 19), ((12, 25), (8, 32), (6, 42)))
        self.add_bezier('bristle-right', (6, 42), ((16, 40), (23, 36), (29, 30)))
        self.add_contour('bristles', 'bristle-left', 'bristle-right')
        join('bristles', 'ferrule')
