"""Robot Gripper above Conveyor Parcel.

Symbol plan: A hanging two-pronged gripper holds a parcel over a capsule conveyor. The tall envelope gives the grip, parcel and belt distinct space. Shared corner contacts describe the actual grip; tape and roller details are omitted.
Lucide: briefcase-conveyor-belt; original and atomic-debug geometry inspected.
Keyshape: VRECT_L; centerline (8,4)-(40,44); ink (6,2)-(42,46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bf5ea292-fb23-4b2b-a18b-45253ab4dcab'
SOURCE_PATH = 'pictographic-primitives/business/factory assembly line belt arm box_bf5ea292-fb23-4b2b-a18b-45253ab4dcab.svg'
AUTHOR = 'gpt-6'

class RobotGripperAboveConveyorParcel(Solo48):
    icon_id = 'robot-gripper-above-conveyor-parcel'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('factory', 'automation', 'industry', 'manufacturing', 'production', 'machine', 'robot', 'process')

    def build(self):
        self.path('belt',(14,32),(34,32),(40,38,6,6,True),(34,44,6,6,True),(14,44),(8,38,6,6,True),(14,32,6,6,True),closed=True)
        self.path('parcel',(20,16),(28,16),(28,24),(20,24),(20,16),closed=True)
        self.path('gripper',(20,16),(12,10),(24,4),(36,10),(28,16));self.relate('connect','gripper','parcel')

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
