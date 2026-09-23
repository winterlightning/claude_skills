from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9bf20118-a278-4080-979f-4ea937240a2a'
SOURCE_PATH = 'icon_set/work/todo-references/retouch landscape_9bf20118-a278-4080-979f-4ea937240a2a.svg'
AUTHOR = 'gpt-6'
# Construction plan: Landscape frame, sun and two mountain peaks with retouch rays outside upper right corner.
# Reference reduction: Reduced retouch rays to three and omitted redundant mountain baseline.
# Construction references: ['wand-sparkles', 'table']

class AuthoredIcon(Solo48):
    icon_id = 'retouch-landscape'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('retouch', 'landscape')

    def build(self):
        self.add_polyline('frame',(27,12),(6,12),(6,42),(42,42),(42,25))
        self.circle('sun',16,22,3)
        self.add_polyline('mountains',(13,34),(20,27),(26,34),(33,23),(38,34))
        self.add_line('wand',(34,14),(42,22))
        for n,a,b in [('ray-top',(34,6),(34,8)),('ray-right',(42,10),(40,12)),('ray-left',(26,6),(28,8))]: self.add_line(n,a,b)

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
