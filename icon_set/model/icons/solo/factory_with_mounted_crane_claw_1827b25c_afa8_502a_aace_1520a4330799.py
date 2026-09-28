"""Factory with Mounted Crane Claw.

Symbol plan: A crane column rises from a one-tooth factory roof and carries a small hanging claw. Keep the circular pivot and physical roof attachment. The second tooth, doorway, windows and double link outlines are omitted for clear spacing.
Lucide: robot-arm; original and atomic-debug geometry inspected.
Keyshape: SQUARE; centerline (6,6)-(42,42); ink (4,4)-(44,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1827b25c-afa8-502a-aace-1520a4330799'
SOURCE_PATH = 'pictographic-primitives/business/factory building crane arm_1827b25c-afa8-502a-aace-1520a4330799.svg'
AUTHOR = 'gpt-6'

class FactoryWithMountedCraneClaw(Solo48):
    icon_id = 'factory-with-mounted-crane-claw'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('factory', 'automation', 'industry', 'manufacturing', 'production', 'machine', 'robot', 'process')

    def build(self):
        self.path('factory',(6,42),(6,34),(22,26),(22,34),(38,34),(42,34),(42,42),(6,42),closed=True)
        self.circle('joint',38,10,4)
        self.add_line('column',(38,14),(38,34));self.relate('connect','column','joint');self.relate('connect','column','factory')
        self.add_line('arm',(34,10),(20,10));self.relate('connect','arm','joint')
        self.path('claw',(14,18),(12,14),(20,10),(28,14),(26,18));self.relate('connect','claw','arm')

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
