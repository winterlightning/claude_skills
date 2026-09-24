"""rectangle two persons: standalone batch 17 repair.
Retained two equal people and the panel. Reduced both heads and shoulder arches together. Head centers (16,19) and (32,19), radius 2; shoulder apex y29, exactly four units of visible detached clearance.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'd96343a5-e841-44ec-86db-6217d2856341'
SOURCE_PATH = 'pictographic-primitives/other/rectangle two persons_d96343a5-e841-44ec-86db-6217d2856341.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'users'
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'

class Drawing(Solo48):
    icon_id='rectangle-two-persons'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('rectangle', 'two', 'persons')

    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def box(self,name,x,y,w,h,r=3):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        members=[]
        for i,a in enumerate(pts):
            b=pts[(i+1)%8];part=f'{name}-{i}';members.append(part)
            if i%2:self.add_arc(part,a,b,radius_x=r)
            else:self.add_line(part,a,b)
        self.add_contour(name,*members,closed=True)

    def bust(self,name,cx,cy,r,shoulder_half_width,shoulder_height):
        # Shared human reference: body apex exactly 8 below head outline.
        self.circle(name+'-head',cx,cy,r)
        apex=cy+r+8;end_y=apex+shoulder_height
        self.add_arc(name+'-shoulders',(cx-shoulder_half_width,end_y),(cx+shoulder_half_width,end_y),radius_x=shoulder_half_width,radius_y=shoulder_height)



    def build(self):
        self.box('panel',4,8,40,32,4)
        for name,cx in (('left',16),('right',32)):self.bust(name,cx,19,2,3,2)

