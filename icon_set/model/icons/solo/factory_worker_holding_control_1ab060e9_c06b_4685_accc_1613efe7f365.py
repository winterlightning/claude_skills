"""Factory Worker Holding Control.

Symbol plan: A worker holds a long control with a bent arm. Circular head and curved shoulders follow human_ref/user.svg with an exact 4-unit detached gap. Omit the cap and sleeve seam; preserve the asymmetric arm action.
Lucide: hand; original and atomic-debug geometry inspected.
Keyshape: HRECT_L; centerline (4,8)-(44,40); ink (2,6)-(46,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1ab060e9-c06b-4685-accc-1613efe7f365'
SOURCE_PATH = 'pictographic-primitives/business/factory manufacturing control_1ab060e9-c06b-4685-accc-1613efe7f365.svg'
AUTHOR = 'gpt-6'

class FactoryWorkerHoldingControl(Solo48):
    icon_id = 'factory-worker-holding-control'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('factory', 'automation', 'industry', 'manufacturing', 'production', 'machine', 'robot', 'process')

    def build(self):
        self.circle('head',30,14,6)
        self.path('shoulder',(24,30),(30,28,26,28,28,28),(44,40,38,28,44,34))
        self.path('arm',(24,30),(20,36),(12,28));self.relate('connect','arm','shoulder')
        self.path('control',(6,20),(10,20),(12,22,2,2,True),(12,28),(12,34),(10,36,2,2,True),(6,36),(4,34,2,2,True),(4,22),(6,20,2,2,True),closed=True);self.relate('connect','arm','control')

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
