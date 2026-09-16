"""Arrow Down with Dashed Upper Shaft.

Symbol plan: A broad arrow has two matching interrupted shaft edges. A single upper dash on each side replaces multiple tiny dashes; the solid lower outline owns the shoulders and tip.
Lucide: arrow-big-down-dash; original and atomic-debug geometry inspected.
Keyshape: VRECT_L; centerline (8,4)-(40,44); ink (6,2)-(42,46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7750e50b-5f52-4c80-8612-46463414b646'
SOURCE_PATH = 'pictographic-primitives/arrows/download dash arrow_7750e50b-5f52-4c80-8612-46463414b646.svg'
AUTHOR = 'gpt-6'

class ArrowDownWithDashedUpperShaft(Solo48):
    icon_id = 'arrow-down-with-dashed-upper-shaft'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'direction', 'navigation', 'pointer', 'movement', 'route', 'flow', 'orientation')

    def build(self):
        for n,x in [('left',20),('right',28)]:self.add_line(n+'-dash',(x,4),(x,8))
        self.path('arrow',(20,16),(20,26),(8,26),(24,44),(40,26),(28,26),(28,16))

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
