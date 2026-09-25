"""Digital Face with Input Nodes.

Symbol plan: A circular digital face receives three equal input nodes. Two eyes and a short neutral mouth preserve face recognition; the construction grid and curved smile are simplified to maintain clear spacing.
Lucide: brain-circuit; original and atomic-debug geometry inspected.
Keyshape: HRECT_L; centerline (4,8)-(44,40); ink (2,6)-(46,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5e37ff04-4c02-4607-a4b2-b81aa6048524'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/deepfake face_5e37ff04-4c02-4607-a4b2-b81aa6048524.svg'
AUTHOR = 'gpt-6'


class DigitalFaceWithInputNodes(Solo48):
    icon_id = 'digital-face-with-input-nodes'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'artificial-intelligence'
    aliases = ()
    keywords = ('head', 'neural network', 'intelligence', 'connection', 'thinking', 'technology', 'brain', 'artificial intelligence')

    def build(self):
        x,y,r=30,24,14
        self.circle('face',x,y,r)
        for n,ex in [('left',26),('right',34)]:self.add_dot(n+'-eye',(ex,20))
        self.add_line('mouth',(26,28),(34,28))
        for j,ny,end in [(0,10,(30,10)),(1,24,(16,24)),(2,38,(30,38))]:
            self.circle(f'node-{j}',6,ny,2)
            self.add_line(f'input-{j}',(8,ny),end);self.relate('connect',f'input-{j}',f'node-{j}');self.relate('connect',f'input-{j}','face')

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
