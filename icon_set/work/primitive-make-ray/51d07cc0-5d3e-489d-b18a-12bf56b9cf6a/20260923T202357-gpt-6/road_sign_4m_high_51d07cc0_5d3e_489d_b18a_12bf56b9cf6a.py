from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '51d07cc0-5d3e-489d-b18a-12bf56b9cf6a'
SOURCE_PATH = 'icon_set/work/todo-references/road sign 4m high_51d07cc0-5d3e-489d-b18a-12bf56b9cf6a.svg'
AUTHOR = 'gpt-6'
# Construction plan: Hand-authored 4M height text between upper and lower chevrons.
# Reference reduction: No defining parts omitted.
# Construction references: ['arrow-right']

class AuthoredIcon(Solo48):
    icon_id = 'road-sign-4m-high'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('road', 'sign', '4m', 'high')

    def build(self):
        self.add_polyline('up',(20,10),(24,6),(28,10))
        self.add_polyline('down',(20,38),(24,42),(28,38))
        self.add_polyline('four',(15,16),(6,29),(19,29))
        self.add_line('four-stem',(15,16),(15,33)); self.relate('connect','four','four-stem')
        self.add_polyline('m',(26,33),(26,17),(34,28),(42,17),(42,33))

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
