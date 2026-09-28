"""Turn Right Arrow. Retains all identifying parts, reconstructed on the integer grid.

HRECT_L visible extremes (2, 6, 46, 42); centerlines (4, 8, 44, 40).
Lucide rotate-cw and undo-2: coherent arcs, open arrowheads and explicit shaft joins.
Mirrored subjects use paired coordinates; directional parts preserve their
intentional asymmetry. Geometry is authored directly on SOLO48.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "90bda1dc-4ea8-4d9e-aace-a5784e398b7c"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__arrow-turn-right/20260926T085631Z-thuan-mac/reference/arrow turn right_90bda1dc-4ea8-4d9e-aace-a5784e398b7c.svg"
AUTHOR = "claude-opus-5-5"


class ArrowTurnRight(Solo48):
    icon_id = 'arrow-turn-right'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol",)
    aliases = ()
    keywords = ('arrow', 'turn', 'right', 'redirect', 'forward', 'curve', 'direction', 'share')

    def build(self) -> None:
        # Symbol plan (HRECT_L x4..44, y8..40): arrowhead (32,8)-(44,20)-(32,32);
        # shaft y20 back to x22; a wide bend of two tangent cubics reaches the
        # left edge x4 with a vertical tangent, then turns to 45 degrees and runs
        # straight into the tail to (13,40) with no kink.
        self.add_polyline('head', (32, 8), (44, 20), (32, 32))
        self.add_line('shaft', (44, 20), (22, 20))
        self.add_bezier('bend-upper', (22, 20), ((13, 20), (4, 23), (4, 30)))
        self.add_bezier('bend-lower', (4, 30), ((4, 33), (6, 34), (9, 36)))
        self.add_line('tail', (9, 36), (13, 40))
        self.add_contour('body', 'shaft', 'bend-upper', 'bend-lower', 'tail')
        self.relate("connect", 'head', 'body')
