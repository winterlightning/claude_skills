from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '078c527e-7fad-4791-9242-4409c4f071d0'
SOURCE_PATH = 'pictographic-primitives/other/Academic Graduation Cap_078c527e-7fad-4791-9242-4409c4f071d0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'academic-graduation-cap-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('Academic Graduation Cap',)

    def build(self):
        # One rounded enclosure; shared corner radius preserves tangent joins.
        l,t,r,b,rad = (6,6,42,42,4)
        self.add_line('frame-top',(l+rad,t),(r-rad,t))
        self.add_arc('frame-tr',(r-rad,t),(r,t+rad),radius_x=rad)
        self.add_line('frame-right',(r,t+rad),(r,b-rad))
        self.add_arc('frame-br',(r,b-rad),(r-rad,b),radius_x=rad)
        self.add_line('frame-bottom',(r-rad,b),(l+rad,b))
        self.add_arc('frame-bl',(l+rad,b),(l,b-rad),radius_x=rad)
        self.add_line('frame-left',(l,b-rad),(l,t+rad))
        self.add_arc('frame-tl',(l,t+rad),(l+rad,t),radius_x=rad)
        self.add_contour('frame','frame-top','frame-tr','frame-right','frame-br','frame-bottom','frame-bl','frame-left','frame-tl',closed=True)
        # Merge the lower board seam into the cap band: preserve wide brim and crown.
        self.add_polyline('cap',(15,21),(24,15),(33,21),(30,23),(30,31),(24,33),(18,31),(18,23),closed=True)
