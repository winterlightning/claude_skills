"""Cleaning Spray Bottle.
Plan: Asymmetric neck joins left-facing nozzle and rounded broad bottle. Extrema (10,4)-(38,44).
Reference: Original source silhouette; Lucide geometric construction with shared joints and coherent curves.
Reduction: Trigger merged into the curved neck silhouette; label omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e4a8d651-8467-42d2-a239-9ad5acf4202c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/farming/sprinkle bottle_e4a8d651-8467-42d2-a239-9ad5acf4202c.svg'
AUTHOR = 'gpt-6'

class Batch27Icon(Solo48):
    icon_id = 'trigger-spray-bottle-curved-neck'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "farming"
    aliases = ()
    keywords = ('cleaning', 'spray', 'bottle')

    def build(self):

        self.add_line('head-1',(10,12),(10,4))
        self.add_line('head-2',(10,4),(30,4))
        self.add_line('head-3',(30,4),(38,12))
        self.add_line('head-4',(38,12),(30,16))
        self.add_bezier('right-neck',(30,16),((30,26),(38,26),(38,34)))
        self.add_line('right',(38,34),(38,38))
        self.add_arc('br',(38,38),(32,44),radius_x=6)
        self.add_line('base',(32,44),(16,44))
        self.add_arc('bl',(16,44),(10,38),radius_x=6)
        self.add_line('left',(10,38),(10,34))
        self.add_bezier('left-neck',(10,34),((10,26),(22,26),(22,12)))
        self.add_line('head-base',(22,12),(10,12))
        self.add_contour('bottle','head-1','head-2','head-3','head-4','right-neck','right','br','base','bl','left','left-neck','head-base',closed=True)
