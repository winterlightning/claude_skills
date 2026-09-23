from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '078c527e-7fad-4791-9242-4409c4f071d0'
SOURCE_PATH = 'icon_set/work/todo-references/Academic Graduation Cap_078c527e-7fad-4791-9242-4409c4f071d0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'academic-graduation-cap'
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
        # Mirrored diamond and cap band share their attachment nodes.
        axis=24
        self.add_polyline('mortarboard',(14,22),(axis,16),(34,22),(29,25),(axis,28),(19,25),closed=True)
        self.add_polyline('band',(19,25),(19,32),(axis,34),(29,32),(29,25))
        self.relate('connect','mortarboard','band')
