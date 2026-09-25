'Ionic column capital with paired circular volutes and three shaft strokes. SQUARE centerlines (6,6)-(42,42). Mirrored curls share radii; central dash omitted for clearance. Lucide landmark informs repeated shaft rhythm.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '78546722-f2d3-45ff-a469-2afaf6a268c0'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-04/historical building pillar_78546722-f2d3-45ff-a469-2afaf6a268c0.svg'
AUTHOR = 'gpt-6'

class IonicColumnCapital(Solo48):
    icon_id = 'ionic-column-capital'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "landmarks"
    aliases = ()
    keywords = ('column', 'pillar', 'ionic', 'capital', 'volute', 'classical', 'greek', 'roman', 'architecture')

    def build(self) -> None:
        axis, top, bottom = 24, 6, 42
        self.add_line('abacus',(14,top),(34,top))
        for side,cx,sweep in [('left',14,False),('right',34,True)]:
            self.add_arc(side+'-outer',(cx,top),(cx,22),radius_x=8,sweep=sweep)
            self.add_arc(side+'-inner',(cx,22),(cx,12),radius_x=5,sweep=sweep)
            self.relate('connect','abacus',side+'-outer')
            self.add_contour(side+'-volute',side+'-outer',side+'-inner')
        for n in range(3):
            x=axis+(n-1)*8
            self.add_line(f'shaft-{n}',(x,31),(x,bottom))
