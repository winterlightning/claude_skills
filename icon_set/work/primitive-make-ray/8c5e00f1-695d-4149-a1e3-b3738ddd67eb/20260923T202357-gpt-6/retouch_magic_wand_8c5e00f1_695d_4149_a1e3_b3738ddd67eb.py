from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8c5e00f1-695d-4149-a1e3-b3738ddd67eb'
SOURCE_PATH = 'icon_set/work/todo-references/retouch magic wand_8c5e00f1-695d-4149-a1e3-b3738ddd67eb.svg'
AUTHOR = 'gpt-6'
# Construction plan: Circular enclosure with diagonal wand and three plus-shaped glints.
# Reference reduction: No defining parts omitted; simplified wand tip.
# Construction references: ['wand-sparkles']

class AuthoredIcon(Solo48):
    icon_id = 'retouch-magic-wand'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('retouch', 'magic', 'wand')

    def build(self):
        self.circle('enclosure',24,24,20)
        self.add_polyline('wand',(12,36),(26,22),(30,26),(16,40),closed=True)
        self.relate('connect','wand','enclosure')
        for n,x,y in [('spark-left',15,16),('spark-top',29,12),('spark-right',36,23)]:
            self.add_line(n+'-h',(x-2,y),(x+2,y)); self.add_line(n+'-v',(x,y-2),(x,y+2)); self.relate('connect',n+'-h',n+'-v')

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
