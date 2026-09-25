"""An arrow sweeps down from upper left into a rightward tip. Square 6..42 supports broad quarter-curve and open head. Source supplies curved downward route; Lucide corner-down-right and arrow-down supply tangent elbow and shared head endpoint. No identity details omitted; arm lengths share 10 units."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '5180aaaf-9d97-4d5e-b398-c79a1c0b5de6'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_14/diagram steady down 1 large head_5180aaaf-9d97-4d5e-b398-c79a1c0b5de6.svg'
AUTHOR = 'gpt-6-astra'
class Drawing(Solo48):
    icon_id = 'arrow-curving-downward-toward-right'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ['Arrow Curving Downward Toward Right']
    keywords = ['arrow', 'curve', 'right', 'down', 'bend', 'direction', 'pointer']
    def build(self):
        self.add_arc('sweep',(6,6),(32,32),radius_x=26,sweep=False)
        self.add_line('end',(32,32),(42,32))
        self.add_contour('shaft','sweep','end')
        self.add_polyline('head',(32,22),(42,32),(32,42))
        self.relate('connect','shaft','head')
