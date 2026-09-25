"""French Pastry Croissant."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f9e55377-8da9-5927-845b-403bea7db251'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/breakfast croissant_f9e55377-8da9-5927-845b-403bea7db251.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'layered-crescent-croissant'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('croissant', 'pastry', 'breakfast', 'bread', 'baking', 'crescent', 'food')

    def build(self):
        # Plan: Crescent croissant with two broad rolled sections. Lucide croissant layered contours; narrow end layers omitted for clearance. Deliberate upward right tilt, envelope (4,8)-(44,40).
        self.add_bezier('outer',(4,27),((4,22),(9,25),(13,24)),((14,16),(24,10),(30,14)),((31,10),(33,8),(36,8)),((41,8),(44,17),(44,23)),((44,26),(42,29),(40,30)),((38,34),(35,36),(33,38)),((29,40),(27,40),(24,40)),((20,40),(16,39),(14,38)),((8,36),(4,32),(4,27)))
        self.add_contour('pastry','outer',closed=True)
        self.add_bezier('roll-seam',(30,14),((26,22),(22,32),(24,40)))
        self.relate('connect','roll-seam','pastry')
