"""A balance weighing a person against money.
Symbol plan and construction: scale: paired pans and central support; human_ref/user.svg: circular head and smooth shoulders.
Keyshape: HRECT_L reserves separate left/right symbol bands above the pans.
Omissions: Small limb steps, triangular pedestal outline and lower dollar tick; the body, pans and base use simpler contours.
Review: Equal pan dimensions and an open dollar curve keep the drawing readable. Head centre (10,11), radius3, head bottom14 and shoulder apex22 give exactly 8 centreline / 4 ink units."""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID='79fff0c7-26d4-4146-b968-24705c1e7d4a'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_39/user cash scale 1_79fff0c7-26d4-4146-b968-24705c1e7d4a.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='user-cash-scale-1'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('user', 'cash', 'scale', '1')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)

    def build(self):
        # Human circle and broad shoulders, exact head-bottom 14 to shoulder-top 22.
        self.circle('head',10,11,3)
        self.add_arc('shoulders',(4,30),(16,30),radius_x=6,radius_y=8)
        for n,cx in [('left',10),('right',38)]:
            self.add_polyline(n+'-rim',(cx-6,30),(cx,30),(cx+6,30))
            self.add_arc(n+'-pan',(cx+6,30),(cx-6,30),radius_x=6,radius_y=8)
            self.relate('connect',n+'-rim',n+'-pan')
        self.relate('connect','shoulders','left-rim')
        self.add_polyline('base',(20,40),(24,40),(28,40))
        self.add_line('stem',(24,40),(24,30))
        self.add_polyline('beam',(16,30),(24,30),(32,30))
        self.relate('connect','stem','base','beam')
        self.relate('connect','beam','left-rim','right-rim')
        self.add_polyline('dollar-top',(40,9),(36,9),(36,8))
        self.add_arc('dollar-upper',(36,9),(36,15),radius_x=3,sweep=False)
        self.add_arc('dollar-lower',(36,15),(36,21),radius_x=3)
        self.add_polyline('dollar-bottom',(32,21),(36,21))
        self.relate('connect','dollar-upper','dollar-top','dollar-lower')
        self.relate('connect','dollar-lower','dollar-bottom')

    def circle(self,name,cx,cy,r):
        pts=[(cx-r,cy),(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy)]
        members=[]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):
            m=f'{name}-{i}';self.add_arc(m,a,b,radius_x=r);members.append(m)
        self.add_contour(name,*members,closed=True)
