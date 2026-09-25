"""A user surrounded by two broadcast arcs.
Symbol plan and construction: radio: nested arcs; human_ref/user.svg: circular head with open shoulders.
Keyshape: SQUARE balances the broadcast span and the small user below.
Omissions: Arm/leg steps and the closed body baseline.
Review: Head centre (24,28), radius3, head bottom31 and shoulder apex39 give exactly 8 centreline / 4 ink units. Broadcast arcs and shoulder contour mirror about x24."""
from ...keyshapes import Keyshape
from icon_set.model.profiles import Profile
from ._base import Solo48
SOURCE_ICON_ID='2000d10a-a193-4355-bf76-3a121de4ad3f'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_39/user signal_2000d10a-a193-4355-bf76-3a121de4ad3f.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='user-signal'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('user', 'signal')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)

    def build(self):
        self.add_arc('signal-outer',(6,24),(42,24),radius_x=18)
        self.add_arc('signal-inner',(16,20),(32,20),radius_x=8,radius_y=4)
        self.circle('head',24,28,3)
        self.add_arc('shoulders',(18,42),(30,42),radius_x=6,radius_y=3)
        # Open shoulder baseline follows human_ref/user.svg; head bottom31, shoulders39.

    def circle(self,name,cx,cy,r):
        pts=[(cx-r,cy),(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy)]
        members=[]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):
            m=f'{name}-{i}';self.add_arc(m,a,b,radius_x=r);members.append(m)
        self.add_contour(name,*members,closed=True)
