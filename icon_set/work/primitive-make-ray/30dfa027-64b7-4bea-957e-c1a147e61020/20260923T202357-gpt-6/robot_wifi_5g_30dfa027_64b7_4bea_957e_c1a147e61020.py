from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '30dfa027-64b7-4bea-957e-c1a147e61020'
SOURCE_PATH = 'icon_set/work/todo-references/robot wifi 5g_30dfa027-64b7-4bea-957e-c1a147e61020.svg'
AUTHOR = 'gpt-6'
# Construction plan: Articulated robot arm with circular joints, open gripper and wireless arcs.
# Reference reduction: Reduced wireless bands to two plus a dot; no 5G text exists in supplied reference.
# Construction references: ['bot', 'rainbow']

class AuthoredIcon(Solo48):
    icon_id = 'robot-wifi-5g'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('robot', 'wifi', '5g')

    def build(self):
        self.circle('base-joint',14,30,6)
        self.circle('wrist',34,16,4)
        self.add_line('arm-top',(17,25),(30,14)); self.add_line('arm-bottom',(20,30),(35,20))
        for n in ('arm-top','arm-bottom'):
            self.relate('connect',n,'base-joint');self.relate('connect',n,'wrist')
        self.add_polyline('support',(12,36),(15,42),(23,42),(20,33));self.relate('connect','support','base-joint')
        self.add_polyline('gripper',(38,16),(42,21),(42,27));self.relate('connect','gripper','wrist')
        self.add_bezier('wifi-outer',(6,10),((11,5),(19,5),(24,10)))
        self.add_bezier('wifi-inner',(11,16),((14,13),(17,13),(20,16)))
        self.add_dot('wifi-point',(16,21))

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
