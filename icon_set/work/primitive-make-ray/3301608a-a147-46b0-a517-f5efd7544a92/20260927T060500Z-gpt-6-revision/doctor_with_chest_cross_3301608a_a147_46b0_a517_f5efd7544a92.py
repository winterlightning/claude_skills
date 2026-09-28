"""Doctor with Chest Cross.

Symbol plan: A circular head floats above a domed torso with a medical chest cross. The shoulders follow human_ref/user.svg and have exactly 4 units of detached ink clearance.
Lucide: user-round; original and atomic-debug geometry inspected.
Keyshape: VRECT_L; centerline (8,4)-(40,44); ink (6,2)-(42,46).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '3301608a-a147-46b0-a517-f5efd7544a92'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__doctor-with-chest-cross/20260927T060349Z-thuan-mac-1/reference/doctor man 1_3301608a-a147-46b0-a517-f5efd7544a92.svg'
AUTHOR = "gpt-6"


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
        self.circle('head',24,12,8)
        self.add_arc('left-shoulder',(8,44),(24,28),radius_x=16)
        self.add_arc('right-shoulder',(24,28),(40,44),radius_x=16)
        self.add_contour('torso','left-shoulder','right-shoulder')
        self.add_line('cross-vertical',(24,37),(24,42))
        self.add_line('cross-horizontal',(20,40),(28,40))
        self.relate('connect','cross-horizontal','cross-vertical')
        self.mark_human_figure('person',head='head',torso='right-shoulder',torso_junction='start')

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
