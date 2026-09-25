"""Shower Head with Falling Water.
Plan: Arched pipe owns the head attachment at (16,14); water remains detached. Ink (6,2)-(42,46).
Construction reference: shower-head.
Reduction: Use three upper water strokes and one lower droplet.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd29f054a-b9d2-5867-b241-ab327c410247'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hotels/bathroom shower_d29f054a-b9d2-5867-b241-ab327c410247.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'shower-head-with-falling-water'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'hotels'
    aliases = ()
    keywords = ('shower', 'head', 'with', 'falling', 'water')
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

        for x in (8,16,24): self.add_line(f'water-{x}',(x,31),(x,34))
        self.add_dot('water-lower',(16,42))
