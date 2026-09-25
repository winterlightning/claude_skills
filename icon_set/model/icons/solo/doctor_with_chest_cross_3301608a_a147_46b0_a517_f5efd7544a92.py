"""Doctor with Chest Cross.

Symbol plan: A circular head floats above a domed torso with a medical chest cross. The shoulders follow human_ref/user.svg and have exactly 4 units of detached ink clearance.
Lucide: user-round; original and atomic-debug geometry inspected.
Keyshape: VRECT_L; centerline (8,4)-(40,44); ink (6,2)-(42,46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3301608a-a147-46b0-a517-f5efd7544a92'
SOURCE_PATH = 'pictographic-primitives/combination/doctor man 1_3301608a-a147-46b0-a517-f5efd7544a92.svg'
AUTHOR = 'gpt-6'


class DoctorWithChestCross(Solo48):
    icon_id = 'doctor-with-chest-cross'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'combination'
    categories = ('combination', 'primitives')
    aliases = ()
    keywords = ('doctor', 'nurse', 'medical', 'healthcare', 'person', 'profession', 'clinic', 'portrait')

    def build(self):
        axis=24
        self.circle('head',axis,10,6)
        self.path('torso',(8,44),(8,40),(axis,24,16,16,True),(40,40,16,16,True),(40,44))
        self.path('cross-vertical',(axis,33),(axis,37),(axis,41))
        self.path('cross-horizontal',(20,37),(axis,37),(28,37));self.relate('connect','cross-horizontal','cross-vertical')

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
