"""Water Treatment Tanks and Connecting Pipes.

Symbol plan: A round vessel and two unequal treatment columns connect through explicit pipes. Omit liquid levels, ladder marks and duplicate tank legs; shared connection points preserve the processing network.
Lucide: cylinder; original and atomic-debug geometry inspected.
Keyshape: HRECT_L; centerline (4,8)-(44,40); ink (2,6)-(46,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '642b50b6-4c0c-402a-8e2c-f06e23fffcb5'
SOURCE_PATH = 'pictographic-primitives/business/factory building water treatment_642b50b6-4c0c-402a-8e2c-f06e23fffcb5.svg'
AUTHOR = 'gpt-6'

class WaterTreatmentTanksAndConnectingPipes(Solo48):
    icon_id = 'water-treatment-tanks-and-connecting-pipes'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('water treatment', 'tank', 'pipe', 'plant', 'processing', 'utility', 'infrastructure', 'industry')

    def build(self):
        self.circle('tank',8,30,4);self.add_line('tank-leg',(8,34),(8,40));self.relate('connect','tank-leg','tank')
        for n,x,y in [('tall',20,8),('short',36,16)]:
            self.path(n+'-column',(x,40),(x,30),(x,20),(x,y+4),(x+4,y,4,4,True),(x+8,y+4,4,4,True),(x+8,20),(x+8,30),(x+8,40),(x,40),closed=True)
        self.add_line('tank-pipe',(12,30),(20,30));self.relate('connect','tank-pipe','tank');self.relate('connect','tank-pipe','tall-column')
        self.add_line('column-pipe',(28,20),(36,20));self.relate('connect','column-pipe','tall-column');self.relate('connect','column-pipe','short-column')

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
