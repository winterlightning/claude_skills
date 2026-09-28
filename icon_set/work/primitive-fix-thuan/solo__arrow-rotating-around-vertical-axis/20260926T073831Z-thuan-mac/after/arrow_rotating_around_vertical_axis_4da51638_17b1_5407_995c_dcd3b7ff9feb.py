"""Arrow Rotating around Vertical Axis.

Symbol plan: A broad elliptical return curves around the vertical axis, ending in mirrored inward-pointing arrowheads. Shared cubic tangents keep the upper turns smooth; the crossing uses an explicit axis junction.
Lucide: rotate-3d; original and atomic-debug geometry inspected.
Keyshape: VRECT_L; centerline (8,4)-(40,44); ink (6,2)-(42,46).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '4da51638-17b1-5407-995c-dcd3b7ff9feb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__arrow-rotating-around-vertical-axis/20260926T073831Z-thuan-mac/reference/d rotation y axis_4da51638-17b1-5407-995c-dcd3b7ff9feb.svg'
AUTHOR = 'claude-opus-5-5'


class ArrowRotatingAroundVerticalAxis(Solo48):
    icon_id = 'arrow-rotating-around-vertical-axis'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('arrow', 'direction', 'navigation', 'pointer', 'movement', 'route', 'flow', 'orientation')

    def build(self):
        # Redraw (no reviewer text; matched to the reference): a vertical axis x 24 from 8 to 40
        # and a wide, shallow rotation sweep around it - an ellipse (rx 20, ry 10, centre
        # (24, 26)) drawn the long way from its upper-left point (12, 18) under the axis to its
        # upper-right point (36, 18), where it is heading back behind the axis. A Lucide-style
        # square arrowhead sits on that end: arms right to (41, 18) and down to (36, 23). The axis
        # crosses the sweep at its lowest point (24, 36), where both are split and joined.
        # (A half-ellipse version read as a trident: attempts/v1-half-ellipse.svg.)
        self.add_line('axis-upper', (24, 8), (24, 36))
        self.add_line('axis-lower', (24, 36), (24, 40))
        self.add_contour('axis', 'axis-upper', 'axis-lower')
        self.add_arc('sweep-left', (12, 18), (24, 36), radius_x=20, radius_y=10, sweep=False)
        self.add_arc('sweep-right', (24, 36), (36, 18), radius_x=20, radius_y=10, sweep=False)
        self.add_contour('sweep', 'sweep-left', 'sweep-right')
        self.add_polyline('arrowhead', (41, 18), (36, 18), (36, 23))
        self.relate('connect', 'axis', 'sweep')
        self.relate('connect', 'sweep', 'arrowhead')
