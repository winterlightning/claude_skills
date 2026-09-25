"""Shower on Arched Pipe.
Plan: Arched pipe owns the head attachment at (16,14); water remains detached. Ink (6,2)-(42,46).
Construction reference: shower-head.
Reduction: Retain the source essentials.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ca06cd0a-9503-578e-a200-75e4966cbab1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hotels/bathroom shower_ca06cd0a-9503-578e-a200-75e4966cbab1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'shower-on-arched-pipe'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'hotels'
    categories = ('hotels', 'primitives')
    aliases = ()
    keywords = ('shower', 'on', 'arched', 'pipe')
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

        self.add_arc('pipe-arch',(16,14),(40,14),radius_x=12,radius_y=10)
        self.add_line('pipe-upright',(40,14),(40,44))
        self.add_contour('pipe','pipe-arch','pipe-upright')
        self.add_arc('head-left',(8,22),(16,14),radius_x=8)
        self.add_arc('head-right',(16,14),(24,22),radius_x=8)
        self.add_line('head-base',(24,22),(8,22))
        self.add_contour('head','head-left','head-right','head-base',closed=True)
        self.relate('connect','head','pipe')

        self.add_line('stream',(16,31),(16,36))
        self.add_line('base',(28,44),(40,44))
        self.relate('connect','base','pipe')
