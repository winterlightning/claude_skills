'Target: round ring with four equal cardinal ticks joined at exact endpoints; centred geometry retained.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3ff85295-bc70-4db2-bf5d-2efaa7b0cead'
SOURCE_PATH = 'icons-json/war/target_3ff85295-bc70-4db2-bf5d-2efaa7b0cead.json'
AUTHOR = 'gpt-6'

class Target3ff85295(Solo48):
    icon_id = 'target-3ff85295'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    aliases = ()
    keywords = ('target', 'war')

    def build(self) -> None:
        # Four equal quarters expose the true cardinal attachment nodes.
        radius = 16
        points = ((24-radius,24),(24,24-radius),(24+radius,24),(24,24+radius))
        for i in range(4):
            self.add_arc(f'rim-{i}',points[i],points[(i+1)%4],radius_x=radius)
        self.add_contour('rim',*(f'rim-{i}' for i in range(4)),closed=True)

        for i,(dx,dy) in enumerate(((-1,0),(0,-1),(1,0),(0,1))):
            self.add_line(f'tick-{i}',(24+dx*radius,24+dy*radius),(24+dx*18,24+dy*18))
            self.relate('connect',f'tick-{i}','rim')
