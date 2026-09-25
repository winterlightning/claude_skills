"""Articulated Robot Arm with Claw.

Symbol plan: A pedestal supports two circular pivots, an angled link and an open claw. Use single structural links and matching pivot radii; omit double link edges and pedestal seam.
Lucide: robot-arm; original and atomic-debug geometry inspected.
Keyshape: SQUARE; centerline (6,6)-(42,42); ink (4,4)-(44,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1fb28545-516b-53ca-bb19-762ca66e50ce'
SOURCE_PATH = 'pictographic-primitives/business/factory industrial robot arm_1fb28545-516b-53ca-bb19-762ca66e50ce.svg'
AUTHOR = 'gpt-6'

class ArticulatedRobotArmWithClaw(Solo48):
    icon_id = 'articulated-robot-arm-with-claw'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('factory', 'automation', 'industry', 'manufacturing', 'production', 'machine', 'robot', 'process')

    def build(self):
        self.path('base',(6,42),(6,38),(10,34,4,4,True),(14,34),(18,34),(22,38,4,4,True),(22,42),(6,42),closed=True)
        self.circle('joint-a',14,16,4);self.circle('joint-b',34,10,4)
        self.add_line('upright',(14,20),(14,34));self.relate('connect','upright','joint-a');self.relate('connect','upright','base')
        self.add_line('link',(18,16),(30,10));self.relate('connect','link','joint-a');self.relate('connect','link','joint-b')
        self.add_line('wrist',(34,14),(34,20));self.relate('connect','wrist','joint-b')
        self.path('claw',(30,30),(28,26),(34,20),(42,26),(40,30));self.relate('connect','claw','wrist')

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
