"""Sink Vanity beneath Mirror.
Plan: Mirror above basin and cabinet; paired cabinet walls share x limits. Ink (4,4)-(44,44).
Construction reference: bath.
Reduction: Omit drawer handles and drawer division; preserve mirror, faucet, bowl and cabinet.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5e0767e2-3a89-5d1f-a004-fc11f454b3f0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hotels/bathroom mirror cabinet_5e0767e2-3a89-5d1f-a004-fc11f454b3f0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sink-vanity-beneath-mirror'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hotels'
    aliases = ()
    keywords = ('sink', 'vanity', 'beneath', 'mirror')
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

        self.add_polyline('mirror',(6,18),(6,6),(42,6),(42,18))
        self.add_line('rim-left',(6,26),(14,26))
        self.add_line('rim-middle',(14,26),(34,26))
        self.add_line('rim-right',(34,26),(42,26))
        self.add_contour('rim','rim-left','rim-middle','rim-right')
        self.add_arc('bowl',(14,26),(34,26),radius_x=10,radius_y=8,sweep=False)
        self.relate('connect','bowl','rim')
        self.add_polyline('cabinet',(6,26),(6,42),(42,42),(42,26))
        self.relate('connect','cabinet','rim')
        self.add_polyline('faucet',(24,26),(24,16),(28,16))
        self.relate('connect','faucet','rim')
