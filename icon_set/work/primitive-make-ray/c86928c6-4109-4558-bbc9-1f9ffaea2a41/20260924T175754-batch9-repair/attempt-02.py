from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='c86928c6-4109-4558-bbc9-1f9ffaea2a41'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_32/real estate message couple building_c86928c6-4109-4558-bbc9-1f9ffaea2a41.svg'
AUTHOR = 'gpt-6'
PLAN='Two people discuss a house in a speech bubble above them.'
OMISSIONS='Small door omitted; paired busts use identical proportions.'
LUCIDE_REFERENCE='house'
HUMAN_REFERENCE='icon_set/references/human_ref/user.svg'
FULL_BODY_REFERENCE=None
class Drawing(Solo48):
    icon_id='real-estate-message-couple-building'
    keyshape=Keyshape.VRECT_L
    human_construction="bust"
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('real', 'estate', 'message', 'couple', 'building')

    def circle(self,n,x,y,r,ry=None):
        ry=r if ry is None else ry
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r,radius_y=ry)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r,radius_y=ry)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,x,y,w,h,r=3):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        names=[]
        for j,a in enumerate(pts):
            b=pts[(j+1)%8];name=f'{n}-{j}';names.append(name)
            if j%2:self.add_arc(name,a,b,radius_x=r)
            else:self.add_line(name,a,b)
        self.add_contour(n,*names,closed=True)

    def house(self,n,x,y,w,h):
        mid=x+w//2
        self.add_polyline(n,(x,y+8),(mid,y),(x+w,y+8),(x+w,y+h),(x,y+h),closed=True)

    def bust(self,n,x,y,r,shoulder_w,shoulder_h):
        self.circle(n+'-head',x,y,r)
        body_top=y+r+8
        self.add_arc(n+'-shoulders',(x-shoulder_w,body_top+shoulder_h),(x+shoulder_w,body_top+shoulder_h),radius_x=shoulder_w,radius_y=shoulder_h)
        # Exact detached gap: (y+r+8) - (y+r) = 8 centerline / 4 ink.

    def build(self):
        # Portrait envelope (8,4)-(40,44). Bubble owns its tail and open-bottom house;
        # paired tiny circular heads touch centered shoulder ink, as compact busts.
        self.add_polyline('bubble',(8,4),(40,4),(40,26),(28,26),(24,30),(20,26),(8,26),closed=True)
        self.add_polyline('house',(20,18),(20,16),(24,12),(28,16),(28,18))
        for name,x in [('left',13),('right',35)]:
            self.circle(name+'-head',x,36,2)
            self.add_arc(name+'-shoulders',(x-4,44),(x+4,44),radius_x=5)
            self.relate('connect',name+'-head',name+'-shoulders')
