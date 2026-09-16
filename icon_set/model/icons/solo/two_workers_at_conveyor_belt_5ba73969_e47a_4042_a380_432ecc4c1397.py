"""Two Workers at Conveyor Belt.

Symbol plan: Two workers stand behind a capsule conveyor. Circular heads and domed shoulders follow human_ref/user.svg with exactly 4 units of detached ink clearance. Omit caps, sleeve creases and rollers; the body endpoints meet the belt.
Lucide: briefcase-conveyor-belt; original and atomic-debug geometry inspected.
Keyshape: HRECT_L; centerline (4,8)-(44,40); ink (2,6)-(46,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5ba73969-e47a-4042-a380-432ecc4c1397'
SOURCE_PATH = 'pictographic-primitives/business/factory assembly line worker_5ba73969-e47a-4042-a380-432ecc4c1397.svg'
AUTHOR = 'gpt-6'

class TwoWorkersAtConveyorBelt(Solo48):
    icon_id = 'two-workers-at-conveyor-belt'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('factory', 'automation', 'industry', 'manufacturing', 'production', 'machine', 'robot', 'process')

    def build(self):
        self.path('belt',(8,32),(20,32),(28,32),(40,32),(44,36,4,4,True),(40,40,4,4,True),(8,40),(4,36,4,4,True),(8,32,4,4,True),closed=True)
        for n,x in [('left',14),('right',34)]:
            self.circle(n+'-head',x,11,3)
            self.path(n+'-body',(x-6,32),(x-6,28),(x,22,6,6,True),(x+6,28,6,6,True),(x+6,32));self.relate('connect',n+'-body','belt')

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
