"""Divided Panel: An upright rounded square is divided by two horizontal lines into three bands. A short central vertical divider splits only the middle band, creating four empty compartments.

Construction: The rounded panel keeps its three horizontal bands and the single middle-band vertical divider.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '4398fcae-6165-43b0-ba6a-29de2bb44558'
SOURCE_PATH = 'pictographic-primitives/state/slot machine_4398fcae-6165-43b0-ba6a-29de2bb44558.svg'
AUTHOR = 'gpt-6'


class DividedPanelState258(Sub32):
    icon_id = 'divided-panel-state-258'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives/shape'
    aliases = ()
    keywords = ('divided', 'panel', 'upright', 'rounded', 'square', 'horizontal', 'lines', 'bands')

    def build(self):
        def rounded(name,x0,y0,x1,y1,r):
            pts=[(x0+r,y0),(x1-r,y0),(x1,y0+r),(x1,y1-r),(x1-r,y1),(x0+r,y1),(x0,y1-r),(x0,y0+r)]
            for i in range(8):
                a,b=pts[i],pts[(i+1)%8]
                if i%2:self.add_arc(name+str(i),a,b,radius_x=r)
                else:self.add_line(name+str(i),a,b)
            self.add_contour(name,*(name+str(i) for i in range(8)),closed=True)
        rounded('outline',2,2,30,30,3)
        for name,y in (('upper',10),('lower',18)):
            self.add_line(name,(2,y),(30,y))
            self.relate('connect','outline',name)
        self.add_line('middle-divider',(16,10),(16,18))
        self.relate('connect','upper','middle-divider')
        self.relate('connect','lower','middle-divider')
