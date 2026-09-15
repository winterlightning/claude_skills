'Target: round ring with four equal cardinal ticks joined at exact endpoints; centred geometry retained.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fa35ca2e-3882-40aa-94b0-a993fab50043'
SOURCE_PATH = 'pictographic-primitives/war/target_fa35ca2e-3882-40aa-94b0-a993fab50043.svg'
AUTHOR = 'gpt-6'

class TargetFa35ca2e(Solo48):
    icon_id = 'target-fa35ca2e'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    aliases = ()
    keywords = ('target', 'war')

    def build(self) -> None:
        # Four equal quarters expose the true cardinal attachment nodes.
        radius = 14
        points = ((24-radius,24),(24,24-radius),(24+radius,24),(24,24+radius))
        for i in range(4):
            self.add_arc(f'rim-{i}',points[i],points[(i+1)%4],radius_x=radius)
        self.add_contour('rim',*(f'rim-{i}' for i in range(4)),closed=True)

        for i,(dx,dy) in enumerate(((-1,0),(0,-1),(1,0),(0,1))):
            self.add_polyline(f'tick-{i}',(24+dx*10,24+dy*10),(24+dx*radius,24+dy*radius),(24+dx*18,24+dy*18))
            self.relate('connect',f'tick-{i}','rim')
