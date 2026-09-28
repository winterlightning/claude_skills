"""Person with Face Construction Guides.

Symbol plan: A circular study head carries a cross guide above broad shoulders. Guide junctions split the head outline; head-to-shoulder clearance is exactly 4 ink units.
Lucide: scan-face; original and atomic-debug geometry inspected.
Keyshape: SQUARE; centerline (6,6)-(42,42); ink (4,4)-(44,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b67a6986-d5db-40d6-9ea0-f4aab7a422b7'
SOURCE_PATH = 'pictographic-primitives/business/design person_b67a6986-d5db-40d6-9ea0-f4aab7a422b7.svg'
AUTHOR = 'gpt-6'


class PersonWithFaceConstructionGuides(Solo48):
    icon_id = 'person-with-face-construction-guides'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    categories = ('business', 'state')
    aliases = ()
    keywords = ('face', 'head', 'portrait', 'guidelines', 'alignment', 'facial recognition', 'landmarks', 'identity')

    def build(self):
        x,y,r=24,16,10
        self.circle('head',x,y,r)
        self.path('horizontal-guide',(6,y),(x-r,y),(x,y),(x+r,y),(42,y));self.relate('connect','head','horizontal-guide')
        self.add_line('vertical-guide',(x,y-r),(x,y));self.relate('connect','vertical-guide','head');self.relate('connect','vertical-guide','horizontal-guide')
        self.path('shoulders',(6,42),(24,34,18,8,True),(42,42,18,8,True))

    def path(self, name, start, *steps, closed=False):
        members=[]
        point=start
        for index, step in enumerate(steps):
            member=f"{name}-{index+1}"
            if len(step)==2:
                self.add_line(member,point,step)
                point=step
            elif len(step)==5:
                x,y,rx,ry,sweep=step
                self.add_arc(member,point,(x,y),radius_x=rx,radius_y=ry,sweep=sweep)
                point=(x,y)
            else:
                x,y,cx1,cy1,cx2,cy2=step
                self.add_bezier(member,point,((cx1,cy1),(cx2,cy2),(x,y)))
                point=(x,y)
            members.append(member)
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.path(name,(x,y-r),(x+r,y,r,r,True),(x,y+r,r,r,True),
                  (x-r,y,r,r,True),(x,y-r,r,r,True),closed=True)

    def rect(self,name,x,y,w,h,r=2):
        self.path(name,(x+r,y),(x+w-r,y),(x+w,y+r,r,r,True),
                  (x+w,y+h-r),(x+w-r,y+h,r,r,True),(x+r,y+h),
                  (x,y+h-r,r,r,True),(x,y+r),(x+r,y,r,r,True),closed=True)
