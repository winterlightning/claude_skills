"""Uniform 4px complete-composition repair candidate; strict findings are retained."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ...primitives import Bezier, Point
SOURCE_ICON_ID = '809bf53d-f979-4aa8-bf75-748eb9b9dacd'
SOURCE_PATH = 'pictographic-primitives/other/circle bluetooth_809bf53d-f979-4aa8-bf75-748eb9b9dacd.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('complete circle', 'vertical Bluetooth stem', 'upper and lower triangles', 'two diagonal left arms')
class Drawing(Sub32):
    icon_id = 'bluetooth-circle-sub32-clean'
    variant_of = 'bluetooth-circle-sub32'
    variant_label = 'Complete 4px cleanup'
    REPAIR_PLAN = {'concept': 'Bluetooth Wireless Connectivity Symbol', 'core_parts': ('complete circle', 'vertical Bluetooth stem', 'upper and lower triangles', 'two diagonal left arms'), 'flexible_parts': 'Coordinates and proportions only; no original elements removed.', 'repair': 'Balance both Bluetooth openings and move the right tips clear of the surrounding circle.'}
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    TYPEFACE_GLYPH_IDS = ()
    def build(self):
        self.circle('frame',16,16,14)
        self.add_line('stem',(15,8),(15,24))
        self.add_polyline('upper',(15,8),(22,12),(10,21))
        self.add_polyline('lower',(10,11),(22,20),(15,24))
        self.relate('connect','stem','upper-1','upper-2','lower-1','lower-2')
        self.relate('connect','upper-2','lower-1')

    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

