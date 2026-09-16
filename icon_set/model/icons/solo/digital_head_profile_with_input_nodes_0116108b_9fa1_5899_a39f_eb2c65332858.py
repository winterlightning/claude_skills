"""Digital Head Profile with Input Nodes.

Symbol plan: An open-backed head profile receives three equal input nodes. Use a rounded crown, deliberate nose corner and one rounded jaw; omit facial details.
Lucide: brain-circuit; original and atomic-debug geometry inspected.
Keyshape: SQUARE; centerline (6,6)-(42,42); ink (4,4)-(44,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0116108b-9fa1-5899-a39f-eb2c65332858'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/deepfake ai_0116108b-9fa1-5899-a39f-eb2c65332858.svg'
AUTHOR = 'gpt-6'


class DigitalHeadProfileWithInputNodes(Solo48):
    icon_id = 'digital-head-profile-with-input-nodes'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'artificial-intelligence'
    aliases = ()
    keywords = ('head', 'neural network', 'intelligence', 'connection', 'thinking', 'technology', 'brain', 'artificial intelligence')

    def build(self):
        self.path('profile',(22,6),(26,6),(38,18,12,12,True),(42,26),(32,26),(32,34),(26,40,6,6,True),(26,42))
        for j,(y,end) in enumerate(((16,24),(28,22),(40,16))):
            self.circle(f'node-{j}',8,y,2)
            self.add_line(f'input-{j}',(10,y),(end,y));self.relate('connect',f'node-{j}',f'input-{j}')

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
