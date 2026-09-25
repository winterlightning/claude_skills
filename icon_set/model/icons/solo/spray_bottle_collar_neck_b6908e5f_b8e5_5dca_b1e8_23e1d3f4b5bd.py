"""Trigger Spray Bottle.
Plan: Left-facing nozzle, angular neck collar and broad rounded bottle. Extrema (10,4)-(38,44).
Reference: Supplied original; no useful exact local Lucide match. Sparse outline and shared attachment principles.
Reduction: Trigger merged with the bent neck; single collar line replaces narrow double band.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b6908e5f-b8e5-5dca-b1e8-23e1d3f4b5bd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/farming/sprinkle bottle_b6908e5f-b8e5-5dca-b1e8-23e1d3f4b5bd.svg'
AUTHOR = 'gpt-6'

class Batch29Icon(Solo48):
    icon_id = 'spray-bottle-collar-neck'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "farming"
    aliases = ()
    keywords = ('trigger', 'spray', 'bottle')

    def build(self):

        self.add_line('head-1',(10, 12),(10, 4))
        self.add_line('head-2',(10, 4),(30, 4))
        self.add_line('head-3',(30, 4),(38, 12))
        self.add_line('head-4',(38, 12),(30, 16))
        self.add_line('neck',(30,16),(30,24))
        self.add_bezier('right-shoulder',(30,24),((30,28),(38,28),(38,34)))
        self.add_line('right',(38,34),(38,38))
        self.add_arc('br',(38,38),(32,44),radius_x=6)
        self.add_line('base',(32,44),(16,44))
        self.add_arc('bl',(16,44),(10,38),radius_x=6)
        self.add_line('left',(10,38),(10,34))
        self.add_bezier('left-shoulder',(10,34),((10,28),(22,28),(22,24)))
        self.add_line('left-neck',(22,24),(22,12))
        self.add_line('head-base',(22,12),(10,12))
        self.add_contour('bottle',*[f'head-{i}' for i in range(1,5)],'neck','right-shoulder','right','br','base','bl','left','left-shoulder','left-neck','head-base',closed=True)
        self.add_line('collar',(22,24),(30,24));self.relate('connect','collar','bottle')
