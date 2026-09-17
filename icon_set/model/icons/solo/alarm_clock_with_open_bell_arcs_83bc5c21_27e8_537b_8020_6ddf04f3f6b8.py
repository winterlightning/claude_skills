"""Alarm Clock with Open Bell Arcs.
Plan: Clock circle with bilateral open bell arcs and feet; paired geometry about x=24. Ink (4,4)-(44,44).
Construction reference: alarm-clock.
Reduction: Omit secondary dial furniture; preserve upward and leftward hands.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '83bc5c21-27e8-537b-8020-6ddf04f3f6b8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/alarm clock_83bc5c21-27e8-537b-8020-6ddf04f3f6b8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'alarm-clock-with-open-bell-arcs'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    aliases = ()
    keywords = ('alarm', 'clock', 'with', 'open', 'bell', 'arcs')
    def build(self):

        def circle(name, cx, cy, r):
            self.add_arc(name+'-top', (cx-r,cy), (cx+r,cy), radius_x=r)
            self.add_arc(name+'-bottom', (cx+r,cy), (cx-r,cy), radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)
        def rect(name,x,y,w,h,r=2):
            pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r),(x+r,y)]
            for i,(a,b) in enumerate(zip(pts,pts[1:])):
                if i%2: self.add_arc(f'{name}-{i}',a,b,radius_x=r)
                else: self.add_line(f'{name}-{i}',a,b)
            self.add_contour(name,*(f'{name}-{i}' for i in range(8)),closed=True)

        circle('face',24,27,15)
        self.add_polyline('hands',(18,27),(24,27),(24,21))
        self.add_arc('bell-left',(6,12),(12,6),radius_x=6)
        self.add_arc('bell-right',(36,6),(42,12),radius_x=6)
        self.add_line('foot-left',(15,39),(12,42))
        self.add_line('foot-right',(33,39),(36,42))
        self.relate('connect','foot-left','face')
        self.relate('connect','foot-right','face')
