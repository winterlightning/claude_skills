"""Fresh revision of quad-bike.

Original and rejected SVG compared before drawing. The wheels were detached from a narrow motorcycle-like bar; added a broad lower chassis joining the two wheels.
"""
"""A quad bike with dipped saddle, high front handlebar and equal wheels. HRECT_L ink (6,6)-(42,42). Lucide car-front informs coherent body contour; wheel hubs omitted."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b3f07500-0d8f-5bbb-b806-122fe5e29847'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-fix-thuan/solo__quad-bike/20260927T153833Z-thuan-mac-1/reference/atv_b3f07500-0d8f-5bbb-b806-122fe5e29847.svg'
AUTHOR = 'gpt-6'

class QuadBike(Solo48):
    icon_id = 'quad-bike'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('atv', 'quad', 'quad bike', 'off-road', 'vehicle', 'four wheeler', 'offroad', 'motor')

    def build(self) -> None:
        wheel_y, radius = 34, 6
        for side,x in [('rear',10),('front',38)]:
            self.add_arc(side+'-upper',(x-radius,wheel_y),(x+radius,wheel_y),radius_x=radius)
            self.add_arc(side+'-lower',(x+radius,wheel_y),(x-radius,wheel_y),radius_x=radius)
            self.add_contour(side+'-wheel',side+'-upper',side+'-lower',closed=True)
        self.add_polyline('body',(10,18),(16,15),(22,20),(28,20),(32,18),(38,18))
        self.add_line('rear-fork',(10,18),(10,28))
        self.add_line('front-fork',(38,18),(38,28))
        for part,wheel in [('rear-fork','rear-wheel'),('front-fork','front-wheel')]:
            self.relate('connect',part,'body');self.relate('connect',part,wheel)
        self.add_polyline('handlebar',(24,8),(31,8),(37,18))
        self.relate('connect','handlebar','body')
