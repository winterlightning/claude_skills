"""Treatment Tower with Elbow Pipe.

Symbol plan: A tall domed treatment tower stands beside a broad elbow pipe. Concentric elbow radii preserve a constant bore; the tower strip and pipe seams are omitted.
Lucide: cylinder; original and atomic-debug geometry inspected.
Keyshape: SQUARE; centerline (6,6)-(42,42); ink (4,4)-(44,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1cce3ebe-7c9e-4ccd-8f60-7f65d3dd1385'
SOURCE_PATH = 'pictographic-primitives/business/factory building water treatment 1_1cce3ebe-7c9e-4ccd-8f60-7f65d3dd1385.svg'
AUTHOR = 'gpt-6'

class TreatmentTowerWithElbowPipe(Solo48):
    icon_id = 'treatment-tower-with-elbow-pipe'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('water treatment', 'tank', 'pipe', 'plant', 'processing', 'utility', 'infrastructure', 'industry')

    def build(self):
        self.path('tower',(6,42),(6,14),(14,6,8,8,True),(22,14,8,8,True),(22,42),(6,42),closed=True)
        self.path('elbow',(30,22),(38,22),(38,30),(42,34,4,4,False),(42,42),(30,30,12,12,True),(30,22),closed=True)

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
