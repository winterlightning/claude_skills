"""Bottles beneath Filling Line.

Symbol plan: Two equal bottles stand on a capsule conveyor under matched outlets. Reduce three filling stations to two; omit droplets and roller marks. One repeated bottle owns neck, shoulder and base geometry.
Lucide: bottle-wine; original and atomic-debug geometry inspected.
Keyshape: HRECT_L; centerline (4,8)-(44,40); ink (2,6)-(46,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '93f1bef9-1fcc-4064-a3e8-d5fff0d005e8'
SOURCE_PATH = 'pictographic-primitives/business/factory manufacturing process bottle_93f1bef9-1fcc-4064-a3e8-d5fff0d005e8.svg'
AUTHOR = 'gpt-6'

class BottlesBeneathFillingLine(Solo48):
    icon_id = 'bottles-beneath-filling-line'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('factory', 'automation', 'industry', 'manufacturing', 'production', 'machine', 'robot', 'process')

    def build(self):
        self.path('belt',(8,32),(20,32),(28,32),(40,32),(44,36,4,4,True),(40,40,4,4,True),(8,40),(4,36,4,4,True),(8,32,4,4,True),closed=True)
        self.path('line',(4,8),(14,8),(34,8),(44,8))
        for n,x in [('left',8),('right',28)]:
            self.path(n+'-bottle',(x+2,18),(x+10,18),(x+10,22),(x+12,26),(x+12,32),(x,32),(x,26),(x+2,22),(x+2,18),closed=True);self.relate('connect',n+'-bottle','belt')
            self.add_line(n+'-outlet',(x+6,8),(x+6,10));self.relate('connect',n+'-outlet','line')

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
