'Target: round ring with four equal cardinal ticks joined at exact endpoints; centred geometry retained.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '39549a2c-f890-5365-b866-44d3f44ceb57'
SOURCE_PATH = 'pictographic-primitives/business/target center_39549a2c-f890-5365-b866-44d3f44ceb57.svg'
AUTHOR = 'gpt-6'

class TargetCenter(Solo48):
    icon_id = 'target-center'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('target', 'center', 'business')

    def build(self) -> None:
        # Four equal quarters expose the true cardinal attachment nodes.
        radius = 14
        points = ((24-radius,24),(24,24-radius),(24+radius,24),(24,24+radius))
        for i in range(4):
            self.add_arc(f'rim-{i}',points[i],points[(i+1)%4],radius_x=radius)
        self.add_contour('rim',*(f'rim-{i}' for i in range(4)),closed=True)

        self.add_arc('centre-top', (19,24), (29,24), radius_x=5, radius_y=5)
        self.add_arc('centre-bottom', (29,24), (19,24), radius_x=5, radius_y=5)
        self.add_contour('centre', 'centre-top', 'centre-bottom', closed=True)

        for i,(dx,dy) in enumerate(((-1,0),(0,-1),(1,0),(0,1))):
            self.add_polyline(f'tick-{i}',(24+dx*5,24+dy*5),(24+dx*radius,24+dy*radius),(24+dx*18,24+dy*18))
            self.relate('connect',f'tick-{i}','rim')
            self.relate('connect',f'tick-{i}','centre')
