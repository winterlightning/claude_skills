from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0bd98d1c-2291-4610-be55-e9292563a85a'
SOURCE_PATH = 'icon_set/work/todo-references/right to bracket_0bd98d1c-2291-4610-be55-e9292563a85a.svg'
AUTHOR = 'gpt-6'
# Construction plan: Opposed open brackets surrounding a rightward arrow.
# Reference reduction: No defining parts omitted.
# Construction references: ['arrow-right', 'table']

class AuthoredIcon(Solo48):
    icon_id = 'right-to-bracket'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('right', 'to', 'bracket')

    def build(self):
        self.add_polyline('left-bracket',(10,10),(4,10),(4,38),(10,38))
        self.add_polyline('right-bracket',(38,10),(44,10),(44,38),(38,38))
        self.add_line('shaft',(14,24),(34,24))
        self.add_polyline('arrow',(26,16),(34,24),(26,32))
        self.relate('connect','shaft','arrow')

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
