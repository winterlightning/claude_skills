"""Automatic Bottle Filling Nozzle.

Symbol plan: A broad nozzle dispenses above two matching bottles. Reduce three bottles to two and the drop to one round mark; omit labels. One bottle definition preserves equal necks, shoulders and bases.
Lucide: bottle-wine; original and atomic-debug geometry inspected.
Keyshape: SQUARE; centerline (6,6)-(42,42); ink (4,4)-(44,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bc8d9ffd-23d8-4477-a6d2-172cda5ebaf0'
SOURCE_PATH = 'pictographic-primitives/business/factory automated bottle fill_bc8d9ffd-23d8-4477-a6d2-172cda5ebaf0.svg'
AUTHOR = 'gpt-6'

class AutomaticBottleFillingNozzle(Solo48):
    icon_id = 'automatic-bottle-filling-nozzle'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('factory', 'automation', 'industry', 'manufacturing', 'production', 'machine', 'robot', 'process')

    def build(self):
        self.path('nozzle',(6,6),(6,10),(10,14,4,4,False),(24,14),(38,14),(42,10,4,4,False),(42,6))
        self.add_line('outlet',(24,14),(24,16));self.relate('connect','outlet','nozzle');self.add_dot('drop',(24,24))
        for n,x in [('left',6),('right',30)]:
            self.path(n+'-bottle',(x+2,26),(x+10,26),(x+10,30),(x+12,34),(x+12,40),(x+10,42,2,2,True),(x+2,42),(x,40,2,2,True),(x,34),(x+2,30),(x+2,26),closed=True)

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
