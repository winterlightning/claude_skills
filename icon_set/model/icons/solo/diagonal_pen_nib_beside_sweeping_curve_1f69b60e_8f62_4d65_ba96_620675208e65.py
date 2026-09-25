"""Vector Pen Tool Drawing Path.

Symbol plan: Diagonal nib beside a free sweeping stroke; Lucide pen-tool informs polygon and slit. Source deliberately asymmetric. Omit additional breather ring and reduce open holder to two ends.
Keyshape SQUARE; exact visible bounds (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1f69b60e-8f62-4d65-ba96-620675208e65'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/vectors pen draw_1f69b60e-8f62-4d65-ba96-620675208e65.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'diagonal-pen-nib-beside-sweeping-curve'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('vector', 'pen', 'tool', 'drawing', 'path')

    def build(self):
        self.add_polyline('nib',(22,40),(26,18),(34,14),(40,20),(36,32),closed=True)
        self.add_line('slit',(22,40),(30,28));self.relate('connect','slit','nib')
        self.add_line('holder-left',(34,14),(38,8));self.add_line('holder-right',(40,20),(42,16))
        for part in ['holder-left','holder-right']:self.relate('connect',part,'nib')
        self.add_arc('stroke-upper',(6,6),(14,14),radius_x=8)
        self.add_arc('stroke-middle',(14,14),(6,34),radius_x=8,radius_y=20)
        self.add_arc('stroke-lower',(6,34),(14,42),radius_x=8,sweep=False)
        self.add_contour('stroke','stroke-upper','stroke-middle','stroke-lower')
