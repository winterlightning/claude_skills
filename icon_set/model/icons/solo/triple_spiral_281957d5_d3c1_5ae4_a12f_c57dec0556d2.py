"""Three clockwise curling arms meet in a triskelion. Preserve the top and two lower curls, with a shared junction; no useful exact local Lucide match."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '281957d5-d3c1-5ae4-a12f-c57dec0556d2'
SOURCE_PATH = 'pictographic-primitives/religion/spiral_281957d5-d3c1-5ae4-a12f-c57dec0556d2.svg'
AUTHOR = 'gpt-6'

class TripleSpiral(Solo48):
    icon_id = 'triple-spiral'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "religion"
    aliases = ()
    keywords = ('spiral', 'triple', 'triskelion', 'curl', 'symbol', 'rotation')

    def oval(self,name,cx,cy,rx,ry=None):
        ry=rx if ry is None else ry
        self.add_arc(name+'-top',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def build(self) -> None:
        # Square centerline box (6,6)-(42,42); three open, coherent curls.
        self.add_arc('top-stem',(24,26),(16,14),radius_x=8,radius_y=12)
        self.add_arc('top-outer',(16,14),(32,14),radius_x=8)
        self.add_arc('top-inner',(32,14),(28,18),radius_x=4)
        self.add_contour('top-curl','top-stem','top-outer','top-inner')
        self.add_arc('left-stem',(24,26),(14,42),radius_x=10,radius_y=16)
        self.add_arc('left-outer',(14,42),(14,26),radius_x=8)
        self.add_contour('left-curl','left-stem','left-outer')
        self.add_arc('right-stem',(24,26),(42,34),radius_x=18,radius_y=8)
        self.add_arc('right-outer',(42,34),(26,34),radius_x=8)
        self.add_contour('right-curl','right-stem','right-outer')
        for a,b in [('top-curl','left-curl'),('top-curl','right-curl'),('left-curl','right-curl')]:
            self.relate('connect',a,b)
