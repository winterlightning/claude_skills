"""Diagonal Machine Track with Two Wheels.

Symbol plan: A diagonal track surrounds two unequal wheels aligned on x+y=48. Smooth tangent outer curves preserve the housing; the lower wheel sits slightly inward from the end cap to provide certified clearance. Tread marks are omitted.
Lucide: truck; original and atomic-debug geometry inspected.
Keyshape: SQUARE; centerline (6,6)-(42,42); ink (4,4)-(44,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '644f0939-3147-4db6-b0af-b342b3de1e9e'
SOURCE_PATH = 'pictographic-primitives/construction/equipment machine track_644f0939-3147-4db6-b0af-b342b3de1e9e.svg'
AUTHOR = 'gpt-6'

class DiagonalMachineTrackWithTwoWheels(Solo48):
    icon_id = 'diagonal-machine-track-with-two-wheels'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'construction'
    categories = ('construction', 'primitives')
    aliases = ()
    keywords = ('track', 'wheel', 'machinery', 'crawler', 'vehicle', 'tread', 'construction', 'equipment')

    def build(self):
        self.path('track',(6,32),(8,24,6,28,6,26),(22,10),(30,6,24,8,27,6),(42,18,12,12,True),(38,26,42,22,40,24),(24,40),(16,42,22,42,18,42),(6,32,10,10,True),closed=True)
        self.circle('lower-wheel',17,31,2);self.circle('upper-wheel',30,18,3)

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
