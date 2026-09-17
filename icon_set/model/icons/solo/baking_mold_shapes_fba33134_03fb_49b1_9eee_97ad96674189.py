"""Assorted Basic Shapes."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fba33134-03fb-49b1-9eee-97ad96674189'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/molds_fba33134-03fb-49b1-9eee-97ad96674189.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'baking-mold-shapes'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('mold', 'baking', 'cookie cutter', 'star', 'circle', 'heart', 'flower')

    def build(self):
        # Plan: Four empty cookie-cutter outlines in a two-by-two grid. Shared 14-unit envelopes and 8-unit gaps. No exact Lucide match. Bounds (6,6)-(42,42).
        self.add_polyline('star',(13,6),(16,10),(20,11),(18,15),(18,20),(13,18),(8,20),(8,15),(6,11),(10,10),closed=True)
        self.add_arc('circle-top',(28,13),(42,13),radius_x=7)
        self.add_arc('circle-bottom',(42,13),(28,13),radius_x=7)
        self.add_contour('circle','circle-top','circle-bottom',closed=True)
        self.add_bezier('flower',(13,30),((8,26),(4,31),(8,35)),((4,39),(8,44),(13,40)),((18,44),(22,39),(18,35)),((22,31),(18,26),(13,30)))
        self.add_contour('clover','flower',closed=True)
        self.add_bezier('heart',(35,42),((32,39),(28,36),(28,32)),((28,28),(32,26),(35,30)),((38,26),(42,28),(42,32)),((42,36),(38,39),(35,42)))
        self.add_contour('heart-outline','heart',closed=True)
