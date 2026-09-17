"""Analog Clock.
Plan: Circular face radius20 with one continuous asymmetric hand pair. Visible radial radius22.
Construction reference: clock.
Reduction: Omit cardinal ticks and hub outline to preserve clean spacing around the two hands.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '02239e41-5c08-5c59-a65d-1a4042e45034'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/watch time_02239e41-5c08-5c59-a65d-1a4042e45034.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'analog-clock'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    aliases = ()
    keywords = ('analog', 'clock')
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

        circle('face',24,24,20)
        self.add_polyline('hands',(18,20),(24,24),(32,16))
