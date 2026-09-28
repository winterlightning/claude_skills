"""Robot Arm Working on Part.

Symbol plan: A jointed robot reaches a triangular workpiece on a platform. Keep two pivots and the physical tool contact; omit sparks and double link edges to preserve clear space.
Lucide: robot-arm; original and atomic-debug geometry inspected.
Keyshape: SQUARE; centerline (6,6)-(42,42); ink (4,4)-(44,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e6f9d03b-fc9f-4178-83f0-a4d334a4cd42'
SOURCE_PATH = 'pictographic-primitives/business/factory industrial robot assembly line_e6f9d03b-fc9f-4178-83f0-a4d334a4cd42.svg'
AUTHOR = 'gpt-6'

class RobotArmWorkingOnPart(Solo48):
    icon_id = 'robot-arm-working-on-part'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('factory', 'automation', 'industry', 'manufacturing', 'production', 'machine', 'robot', 'process')

    def build(self):
        self.rect('base',6,34,8,8,2);self.circle('joint-a',10,16,4);self.circle('joint-b',34,10,4)
        self.add_line('upright',(10,20),(10,34));self.relate('connect','upright','joint-a');self.relate('connect','upright','base')
        self.add_line('link',(14,16),(30,10));self.relate('connect','link','joint-a');self.relate('connect','link','joint-b')
        self.add_line('tool',(34,14),(34,26));self.relate('connect','tool','joint-b')
        self.path('platform',(22,34),(26,34),(42,34),(42,42),(22,42),(22,34),closed=True)
        self.path('part',(26,34),(34,26),(42,34));self.relate('connect','part','platform');self.relate('connect','part','tool')

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
