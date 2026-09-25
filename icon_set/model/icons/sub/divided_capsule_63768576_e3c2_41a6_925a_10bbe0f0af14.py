"""Divided Capsule: An upright rounded capsule is divided into equal upper and lower halves by a horizontal line. Generate this component alone; exclude Cut-Corner Document Frame.

Construction: An upright rounded capsule is divided halfway by a horizontal line.
Keyshape: VRECT_L; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '63768576-e3c2-41a6-925a-10bbe0f0af14'
SOURCE_PATH = 'pictographic-primitives/state/rtf format_63768576-e3c2-41a6-925a-10bbe0f0af14.svg'
AUTHOR = 'gpt-6'


class DividedCapsule(Sub32):
    icon_id = 'divided-capsule'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('divided', 'capsule', 'upright', 'rounded', 'equal', 'upper', 'lower', 'halves')

    def build(self):
        def rounded(name,x0,y0,x1,y1,r):
            pts=[(x0+r,y0),(x1-r,y0),(x1,y0+r),(x1,y1-r),(x1-r,y1),(x0+r,y1),(x0,y1-r),(x0,y0+r)]
            for i in range(8):
                a,b=pts[i],pts[(i+1)%8]
                if i%2:self.add_arc(name+str(i),a,b,radius_x=r)
                else:self.add_line(name+str(i),a,b)
            self.add_contour(name,*(name+str(i) for i in range(8)),closed=True)
        rounded('outline',6,2,26,30,4)
        self.add_line('divider',(6,16),(26,16))
        self.relate('connect','outline','divider')
