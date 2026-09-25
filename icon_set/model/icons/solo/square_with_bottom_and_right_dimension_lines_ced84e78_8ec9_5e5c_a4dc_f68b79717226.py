"""Square Dimension Measurement.

Symbol plan: Rounded square plus two capped orthogonal dimensions; square side 20; measured edges aligned. Lucide ruler informs terminal marks.
Keyshape: SQUARE; exact visible bounds (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ced84e78-8ec9-5e5c-a4dc-f68b79717226'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/sizing_ced84e78-8ec9-5e5c-a4dc-f68b79717226.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'square-with-bottom-and-right-dimension-lines'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "design"
    aliases = ()
    keywords = ('square', 'dimension', 'measurement')

    def build(self):
        self.rect('square',6,6,20,20)
        for name, coords in [('width',((6,39),(26,39))),('height',((39,6),(39,26)))]:
            a,b=coords
            self.add_line(name,a,b)
            for i,(x,y) in enumerate(coords):
                pts=((x,y-3),(x,y+3)) if name=='width' else ((x-3,y),(x+3,y))
                # Split cap at its shaft attachment.
                self.graph([(f'{name}-cap-{i}-a',pts[0],(x,y)),(f'{name}-cap-{i}-b',(x,y),pts[1])])
                self.relate('connect',name,f'{name}-cap-{i}-a')
                self.relate('connect',name,f'{name}-cap-{i}-b')

    def rect(self, name, x, y, w, h, r=2):
        points=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),
                (x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        ids=[]
        for i,a in enumerate(points):
            b=points[(i+1)%8]; part=f"{name}-{i}"
            if i%2: self.add_arc(part,a,b,radius_x=r)
            else: self.add_line(part,a,b)
            ids.append(part)
        self.add_contour(name,*ids,closed=True)

    def graph(self, edges):
        # Every relation below joins two edges at their shared endpoint.
        for name,a,b in edges: self.add_line(name,a,b)
        for i,(name,a,b) in enumerate(edges):
            for other,c,d in edges[i+1:]:
                if {a,b}&{c,d}: self.relate('connect',name,other)
