"""Tablet with Two Connected Phones.

Symbol plan: A tablet stands behind two connected upright phones. Repeated phones share size; small screen dividers and tablet button are omitted.
Lucide: tablet-smartphone; original and atomic-debug geometry inspected.
Keyshape: SQUARE; centerline (6,6)-(42,42); ink (4,4)-(44,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0132e556-8fca-4176-ada0-9c09e12b3777'
SOURCE_PATH = 'pictographic-primitives/apps/devicefarm ipad_0132e556-8fca-4176-ada0-9c09e12b3777.svg'
AUTHOR = 'gpt-6'


class TabletWithTwoConnectedPhones(Solo48):
    icon_id = 'tablet-with-two-connected-phones'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'apps'
    categories = ('apps', 'primitives')
    aliases = ()
    keywords = ('phone', 'tablet', 'device', 'mobile', 'screen', 'technology', 'communication', 'hardware')

    def build(self):
        self.path('tablet',(18,14),(18,10),(22,6,4,4,True),(38,6),(42,10,4,4,True),(42,38),(38,42,4,4,True),(26,42),(10,42),(6,42))
        for n,x in [('left',6),('right',22)]:
            self.path(n+'-phone',(x+2,22),(x+6,22),(x+8,24,2,2,True),(x+8,32),(x+6,34,2,2,True),(x+4,34),(x+2,34),(x,32,2,2,True),(x,24),(x+2,22,2,2,True),closed=True)
            self.add_line(n+'-cable',(x+4,34),(x+4,42));self.relate('connect',n+'-cable',n+'-phone');self.relate('connect',n+'-cable','tablet')

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
