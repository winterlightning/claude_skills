from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5347ab2e-1381-488a-955c-635749f52970'
SOURCE_PATH = 'icon_set/work/todo-references/restroom outdoor_5347ab2e-1381-488a-955c-635749f52970.svg'
AUTHOR = 'gpt-6'
# Construction plan: Portable restroom with arched roof, inset door and triangular door emblem.
# Reference reduction: Omitted tiny door handle; retained triangular emblem.
# Construction references: ['table']

class AuthoredIcon(Solo48):
    icon_id = 'restroom-outdoor'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('restroom', 'outdoor')

    def build(self):
        self.add_arc('roof',(8,12),(40,12),radius_x=16,radius_y=8)
        self.add_polyline('walls',(40,12),(40,44),(8,44),(8,12))
        self.add_line('roof-seam',(8,12),(40,12))
        self.relate('connect','roof','walls');self.relate('connect','roof-seam','walls');self.relate('connect','roof','roof-seam')
        self.add_polyline('door',(16,44),(16,21),(32,21),(32,44))
        self.relate('connect','door','walls')
        self.add_polyline('emblem',(24,28),(20,35),(28,35),closed=True)

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
