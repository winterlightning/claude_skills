from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '92836afb-27f7-417c-bcab-bbb33f3c2203'
SOURCE_PATH = 'icon_set/work/todo-references/roof house with wrench_92836afb-27f7-417c-bcab-bbb33f3c2203.svg'
AUTHOR = 'gpt-6'
# Construction plan: Roof chevron above a horizontal double open-ended wrench.
# Reference reduction: No defining parts omitted.
# Construction references: ['wrench']

class AuthoredIcon(Solo48):
    icon_id = 'roof-house-with-wrench'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('roof', 'house', 'with', 'wrench')

    def build(self):
        self.add_polyline('roof',(4,24),(24,8),(44,24))
        self.add_bezier('jaw-left',(6,30),((16,25),(19,40),(6,40)))
        self.add_bezier('jaw-right',(42,30),((32,25),(29,40),(42,40)))
        self.add_line('handle',(15,35),(33,35))
        self.relate('connect','handle','jaw-left');self.relate('connect','handle','jaw-right')

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
