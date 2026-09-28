"""Arrow Rising along Dashed Curve.

Symbol plan: Two spaced tail dashes lead into one smoothly accelerating upward curve. The arrowhead remains upright, and the tip owns the curve tangent.
Lucide: trending-up; original and atomic-debug geometry inspected.
Keyshape: SQUARE; centerline (6,6)-(42,42); ink (4,4)-(44,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4c28f22a-efc4-4f1b-bac5-cd4b8669c74c'
SOURCE_PATH = 'pictographic-primitives/arrows/dash steady up_4c28f22a-efc4-4f1b-bac5-cd4b8669c74c.svg'
AUTHOR = 'gpt-6'


class ArrowRisingAlongDashedCurve(Solo48):
    icon_id = 'arrow-rising-along-dashed-curve'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('arrow', 'direction', 'navigation', 'pointer', 'movement', 'route', 'flow', 'orientation')

    def build(self):
        self.add_line('dash-1',(6,42),(10,42))
        self.add_line('dash-2',(20,40),(22,39))
        self.add_bezier('rising-curve',(30,32),((33,26),(34,14),(34,6)))
        self.path('arrowhead',(26,14),(34,6),(42,14));self.relate('connect','arrowhead','rising-curve')

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
