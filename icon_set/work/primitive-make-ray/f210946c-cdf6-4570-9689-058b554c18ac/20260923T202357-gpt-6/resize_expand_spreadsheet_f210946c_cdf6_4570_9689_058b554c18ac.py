from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f210946c-cdf6-4570-9689-058b554c18ac'
SOURCE_PATH = 'icon_set/work/todo-references/resize expand spreadsheet_f210946c-cdf6-4570-9689-058b554c18ac.svg'
AUTHOR = 'gpt-6'
# Construction plan: Spreadsheet with a header and a two-by-two cell array; dimension arrows below and right.
# Reference reduction: Reduced cell count to preserve open cells.
# Construction references: ['table', 'arrow-right']

class AuthoredIcon(Solo48):
    icon_id = 'resize-expand-spreadsheet'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('resize', 'expand', 'spreadsheet')

    def build(self):
        self.box('sheet',6,6,30,30,2)
        for name,a,b in [('header',(6,14),(30,14)),('row',(6,22),(30,22)),('column',(18,14),(18,30))]:
            self.add_line(name,a,b);self.relate('connect',name,'sheet')
        self.relate('connect','header','column');self.relate('connect','row','column')
        self.add_line('vertical',(42,6),(42,30))
        for name,pts in [('up',((38,10),(42,6),(46,10))),('down',((38,26),(42,30),(46,26))),('left',((10,38),(6,42),(10,46))),('right',((26,38),(30,42),(26,46)))]:
            self.add_polyline(name,*pts)
        self.add_line('horizontal',(6,42),(30,42))
        for h in ('up','down'): self.relate('connect',h,'vertical')
        for h in ('left','right'): self.relate('connect',h,'horizontal')

    def circle(self, name, x, y, r):
        self.add_arc(name+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-a',name+'-b',closed=True)

    def box(self, name, l, t, r, b, radius=3):
        q=radius
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q)]
        ids=[]
        for k in range(8):
            ident=f'{name}-{k}'; ids.append(ident)
            a,z=pts[k],pts[(k+1)%8]
            if k%2: self.add_arc(ident,a,z,radius_x=q)
            else: self.add_line(ident,a,z)
        self.add_contour(name,*ids,closed=True)

    def heart(self, name, cx, top, half, bottom):
        # Mirrored lobes and tangent downward shoulders share one outline.
        l=cx-half; r=cx+half; y=top+half//2
        self.add_bezier(name,(cx,top+3),
            ((cx-half//2,top-3),(l,top),(l,y)),
            ((l,y+4),(cx-half//2,bottom-4),(cx,bottom)),
            ((cx+half//2,bottom-4),(r,y+4),(r,y)),
            ((r,top),(cx+half//2,top-3),(cx,top+3)))
