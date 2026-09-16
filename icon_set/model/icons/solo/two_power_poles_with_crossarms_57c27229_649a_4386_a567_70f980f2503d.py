"""Two Power Poles with Crossarms.

Symbol plan: Two unequal poles share a ground line. Crossarms, a forked support and one pair of insulators repeat at two heights; minor posts are reduced.
Lucide: utility-pole; original and atomic-debug geometry inspected.
Keyshape: SQUARE; centerline (6,6)-(42,42); ink (4,4)-(44,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '57c27229-649a-4386-a567-70f980f2503d'
SOURCE_PATH = 'pictographic-primitives/construction/electricity pillar_57c27229-649a-4386-a567-70f980f2503d.svg'
AUTHOR = 'gpt-6'

class TwoPowerPolesWithCrossarms(Solo48):
    icon_id = 'two-power-poles-with-crossarms'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'construction'
    aliases = ()
    keywords = ('power line', 'pylon', 'electricity', 'pole', 'transmission', 'infrastructure', 'energy', 'utility')

    def build(self):
        self.path('ground',(6,42),(16,42),(34,42),(42,42))
        for n,x,y in [('tall',16,12),('short',34,24)]:
            self.path(n+'-pole',(x,y+8),(x,42));self.relate('connect',n+'-pole','ground')
            self.path(n+'-fork',(x-8,y),(x,y+8),(x+8,y));self.relate('connect',n+'-fork',n+'-pole')
            self.path(n+'-bar',(x-8,y),(x+8,y));self.relate('connect',n+'-bar',n+'-fork')
            for j,dx in enumerate((-8,8)):
                self.add_line(f'{n}-post-{j}',(x+dx,y-6),(x+dx,y));self.relate('connect',f'{n}-post-{j}',n+'-bar');self.relate('connect',f'{n}-post-{j}',n+'-fork')

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
