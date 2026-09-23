from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '1bf5b8f8-1714-40eb-bf12-43026ede4d1e'
SOURCE_PATH = 'icon_set/work/todo-references/romance heterosextual symbol_1bf5b8f8-1714-40eb-bf12-43026ede4d1e.svg'
AUTHOR = 'gpt-6'
# Construction plan: Combined male and female sign surrounding a heart.
# Reference reduction: No defining parts omitted.
# Construction references: ['heart', 'arrow-right']

class AuthoredIcon(Solo48):
    icon_id = 'romance-heterosextual-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('romance', 'heterosextual', 'symbol')

    def build(self):
        self.circle('ring',21,24,15)
        self.heart('heart',21,17,7,30)
        self.add_line('male-stem',(32,13),(42,6));self.relate('connect','male-stem','ring')
        self.add_polyline('male-head',(34,6),(42,6),(42,14));self.relate('connect','male-head','male-stem')
        self.add_line('female-stem',(21,39),(21,42));self.relate('connect','female-stem','ring')
        self.add_line('female-cross',(15,42),(27,42));self.relate('connect','female-cross','female-stem')

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
