"""Six Mobile Phones in Grid.

Symbol plan: Six upright phones in a strict two-by-three grid. All phones share one 8-by-12 outline; internal screen bars are removed to preserve clearance.
Lucide: smartphone; original and atomic-debug geometry inspected.
Keyshape: HRECT_L; centerline (4,8)-(44,40); ink (2,6)-(46,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f99e66ec-4007-4de6-af8e-e56fc675139c'
SOURCE_PATH = 'pictographic-primitives/apps/devicefarm_f99e66ec-4007-4de6-af8e-e56fc675139c.svg'
AUTHOR = 'gpt-6'


class SixMobilePhonesInGrid(Solo48):
    icon_id = 'six-mobile-phones-in-grid'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'apps'
    aliases = ()
    keywords = ('phone', 'tablet', 'device', 'mobile', 'screen', 'technology', 'communication', 'hardware')

    def build(self):
        width,height,step_x,step_y=8,12,16,20
        for row in range(2):
            for col in range(3):
                self.rect(f'phone-{row}-{col}',4+col*step_x,8+row*step_y,width,height,2)

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
