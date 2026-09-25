"""Hard Hat with Central Ridge.

Symbol plan: A broad dome and capsule brim surround one raised central ridge. Mirrored sides share radii and exact ridge attachment nodes.
Lucide: hard-hat; original and atomic-debug geometry inspected.
Keyshape: HRECT_L; centerline (4,8)-(44,40); ink (2,6)-(46,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4a9ffb7b-6930-4a9e-bb2e-449c166ffd75'
SOURCE_PATH = 'pictographic-primitives/construction/design helmet_4a9ffb7b-6930-4a9e-bb2e-449c166ffd75.svg'
AUTHOR = 'gpt-6'


class HardHatWithCentralRidge(Solo48):
    icon_id = 'hard-hat-with-central-ridge'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'construction'
    categories = ('construction', 'primitives')
    aliases = ()
    keywords = ('hard hat', 'safety', 'helmet', 'construction', 'protection', 'workwear', 'equipment', 'headgear')

    def build(self):
        self.path('brim',(8,32),(40,32),(44,36,4,4,True),(40,40,4,4,True),(8,40),(4,36,4,4,True),(8,32,4,4,True),closed=True)
        self.path('ridge',(20,23),(20,16),(20,12),(24,8,4,4,True),(28,12,4,4,True),(28,16),(28,23))
        for n,mirror in [('left',False),('right',True)]:
            def p(x,y):return (48-x if mirror else x,y)
            self.path(n+'-dome',p(8,32),p(8,28),(*p(20,16),12,12,not mirror))
            self.relate('connect',n+'-dome','ridge');self.relate('connect',n+'-dome','brim')

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
