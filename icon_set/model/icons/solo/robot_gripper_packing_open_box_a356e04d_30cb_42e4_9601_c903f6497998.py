"""Robot Gripper Packing Open Box.

Symbol plan: A gripper holds an item over an open carton. Grip tips meet the item at shared corners; matched box flaps preserve the open packing scene. Omit tape and gripper joint details.
Lucide: package-open; original and atomic-debug geometry inspected.
Keyshape: VRECT_L; centerline (8,4)-(40,44); ink (6,2)-(42,46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a356e04d-30cb-42e4-9601-c903f6497998'
SOURCE_PATH = 'pictographic-primitives/business/factory manufacturing line packing robot arm_a356e04d-30cb-42e4-9601-c903f6497998.svg'
AUTHOR = 'gpt-6'

class RobotGripperPackingOpenBox(Solo48):
    icon_id = 'robot-gripper-packing-open-box'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('factory', 'automation', 'industry', 'manufacturing', 'production', 'machine', 'robot', 'process')

    def build(self):
        self.path('item',(20,20),(28,20),(28,28),(20,28),(20,20),closed=True)
        self.add_line('shaft',(24,4),(24,8))
        self.path('grip',(20,20),(12,14),(24,8),(36,14),(28,20));self.relate('connect','grip','shaft');self.relate('connect','grip','item')
        self.path('box',(8,26),(12,32),(12,44),(36,44),(36,32),(40,26))

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
