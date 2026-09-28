"""Four-Way Arrow with Central Circle.

Symbol plan: A standalone four-direction control emblem: central circle and four shared arrow definitions. Remove peripheral diamond dashes.
Lucide construction: move; original and atomic-debug inspected.
Keyshape: SQUARE; centerline (6,6)-(42,42); ink (4,4)-(44,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cf23e43e-5ca5-41f0-8a81-0b73f4acf470'
SOURCE_PATH = 'pictographic-primitives/arrows/control tower_cf23e43e-5ca5-41f0-8a81-0b73f4acf470.svg'
AUTHOR = 'gpt-6'


class FourWayArrowWithCentralCircle(Solo48):
    icon_id = 'four-way-arrow-with-central-circle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('four-way', 'arrow', 'with', 'central', 'circle')

    def build(self):
        self.path('hub',(24,20),(28,24,4,4,True),(24,28,4,4,True),(20,24,4,4,True),(24,20,4,4,True),closed=True)
        for name,root,tip,a,b in [('up',(24,20),(24,6),(18,12),(30,12)),('down',(24,28),(24,42),(18,36),(30,36)),('left',(20,24),(6,24),(12,18),(12,30)),('right',(28,24),(42,24),(36,18),(36,30))]:
            self.add_line(name+'-shaft',root,tip);self.path(name+'-head',a,tip,b)
            self.relate('connect',name+'-shaft','hub');self.relate('connect',name+'-shaft',name+'-head')

    def path(self, name, start, *steps, closed=False):
        members=[]
        point=start
        for i, step in enumerate(steps):
            member=f"{name}-{i+1}"
            if len(step)==2:
                self.add_line(member, point, step)
                point=step
            else:
                x,y,rx,ry,sweep=step
                self.add_arc(member, point, (x,y), radius_x=rx, radius_y=ry, sweep=sweep)
                point=(x,y)
            members.append(member)
        self.add_contour(name,*members,closed=closed)

    def circle(self, name, x, y, r):
        self.path(name,(x-r,y),(x+r,y,r,r,True),(x-r,y,r,r,True),closed=True)

    def rect(self, name, x, y, w, h, r=2):
        self.path(name,(x+r,y),(x+w-r,y),(x+w,y+r,r,r,True),
                  (x+w,y+h-r),(x+w-r,y+h,r,r,True),(x+r,y+h),
                  (x,y+h-r,r,r,True),(x,y+r),(x+r,y,r,r,True),closed=True)
