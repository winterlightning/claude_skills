"""Tilting Cement Mixer on Stand.

Symbol plan: A tilted drum sits on a wheeled support and upright handle. Keep the angular loading mouth and rounded drum; omit its narrow rim and internal seams. Intentional tilt preserves the mixing equipment.
Lucide: construction; original and atomic-debug geometry inspected.
Keyshape: VRECT_L; centerline (8,4)-(40,44); ink (6,2)-(42,46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6cc5324d-8f82-5175-9cde-60ad465b6c00'
SOURCE_PATH = 'pictographic-primitives/construction/equipment cement_6cc5324d-8f82-5175-9cde-60ad465b6c00.svg'
AUTHOR = 'gpt-6'

class TiltingCementMixerOnStand(Solo48):
    icon_id = 'tilting-cement-mixer-on-stand'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'construction'
    aliases = ()
    keywords = ('cement mixer', 'concrete', 'mixing', 'construction', 'drum', 'equipment', 'machinery', 'building')

    def build(self):
        self.path('drum',(8,12),(20,4),(28,8),(32,16,31,10,32,12),(32,20),(24,28,8,8,True),(16,26,20,28,18,27),(8,12),closed=True)
        self.circle('wheel',12,40,4)
        self.add_line('leg',(16,26),(12,36));self.relate('connect','leg','drum');self.relate('connect','leg','wheel')
        self.path('stand',(16,40),(40,40),(40,20),(40,12));self.relate('connect','stand','wheel')
        self.add_line('axle',(32,20),(40,20));self.relate('connect','axle','drum');self.relate('connect','axle','stand')

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
