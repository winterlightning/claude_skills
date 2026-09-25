"""Square Distance To Bottom.

Symbol plan: A square at top, integral downward measurement arrow, detached baseline. The arrow measures distance rather than adding an action badge.
Keyshape: SQUARE; exact visible bounds (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '582f7e66-d95a-5051-b785-7bfe8e5eccc4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/bottom distance_582f7e66-d95a-5051-b785-7bfe8e5eccc4.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'square-with-downward-distance-arrow'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "design"
    categories = ("design", "primitives")
    aliases = ()
    keywords = ('square', 'distance', 'to', 'bottom')

    def build(self):
        a=24
        self.add_line('bottom-left',(a,22),(18,22))
        self.add_arc('corner-bl',(18,22),(16,20),radius_x=2)
        self.add_line('left',(16,20),(16,8))
        self.add_arc('corner-tl',(16,8),(18,6),radius_x=2)
        self.add_line('top',(18,6),(30,6))
        self.add_arc('corner-tr',(30,6),(32,8),radius_x=2)
        self.add_line('right',(32,8),(32,20))
        self.add_arc('corner-br',(32,20),(30,22),radius_x=2)
        self.add_line('bottom-right',(30,22),(a,22))
        self.add_contour('box','bottom-left','corner-bl','left','corner-tl','top','corner-tr','right','corner-br','bottom-right',closed=True)
        self.graph([('shaft',(a,22),(a,34)),('arrow-left',(a,34),(18,28)),('arrow-right',(a,34),(30,28))])
        self.relate('connect','box','shaft')
        self.add_line('baseline',(6,42),(42,42))

    def graph(self, edges):
        # Every relation below joins two edges at their shared endpoint.
        for name,a,b in edges: self.add_line(name,a,b)
        for i,(name,a,b) in enumerate(edges):
            for other,c,d in edges[i+1:]:
                if {a,b}&{c,d}: self.relate('connect',name,other)
