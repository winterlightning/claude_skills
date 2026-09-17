"""Half Clock Face.
Plan: Right semicircular face closes along x24; three detached ticks mark the missing left half. Radial envelope22.
Reference construction: clock.
Reduction: Keep the three floating left-side ticks and the right cardinal tick; omit the crowded inner diagonal ticks.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '21de1f87-8bd9-522a-b90b-90cdb99c8025'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/time clock six_21de1f87-8bd9-522a-b90b-90cdb99c8025.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'half-clock-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    aliases = ()
    keywords = ('half', 'clock', 'face')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        self.add_arc('upper',(24,4),(44,24),radius_x=20)
        self.add_arc('lower',(44,24),(24,44),radius_x=20)
        self.add_line('diameter',(24,44),(24,4));self.add_contour('half','upper','lower','diameter',closed=True)
        self.add_line('right-tick',(44,24),(38,24));self.relate('connect','right-tick','half')
        for j,(a,b) in enumerate([((4,24),(8,24)),((10,10),(12,12)),((10,38),(12,36))]):self.add_line(f'tick-{j}',a,b)
