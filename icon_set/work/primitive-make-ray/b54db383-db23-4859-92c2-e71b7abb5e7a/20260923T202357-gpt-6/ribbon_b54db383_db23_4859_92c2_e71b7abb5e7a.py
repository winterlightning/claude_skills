from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b54db383-db23-4859-92c2-e71b7abb5e7a'
SOURCE_PATH = 'icon_set/work/todo-references/ribbon_b54db383-db23-4859-92c2-e71b7abb5e7a.svg'
AUTHOR = 'gpt-6'
# Construction plan: Round award with curved flaring ribbon tails, retaining the reference variant.
# Reference reduction: No defining parts omitted.
# Construction references: ['award']

class AuthoredIcon(Solo48):
    icon_id = 'ribbon'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('ribbon',)

    def build(self):
        self.circle('medal',24,20,16)
        for name,sgn in [('left',-1),('right',1)]:
            def p(x,y): return (24+sgn*x,y)
            self.add_bezier(name,p(10,33),(p(13,35),p(15,38),p(16,40)),(p(12,38),p(10,39),p(9,44)),(p(6,42),p(3,39),p(0,36)))
            self.relate('connect',name,'medal')
        self.relate('connect','left','right')

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
