"""Bow and Arrow.

Plan: Diagonal bow, taut string and arrow with open head and reduced fletching. Circle radius 30 uses integer 18/24 nodes at arrow crossing. Lucide bow-arrow informed structure. Bounds (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0c533236-5c40-40d9-bfbe-74a4e6fe6dcd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/rama navami_0c533236-5c40-40d9-bfbe-74a4e6fe6dcd.svg'
AUTHOR = 'gpt-6'

class BowAndArrowReference(Solo48):
    icon_id = 'bow-and-arrow-reference'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/holidays'
    aliases = ()
    keywords = ('bow', 'and', 'arrow', 'reference')

    def build(self):
        self.add_arc('bow-upper',(6,6),(30,18),radius_x=30)
        self.add_arc('bow-lower',(30,18),(36,36),radius_x=30)
        self.add_contour('bow','bow-upper','bow-lower')
        self.add_polyline('string',(6,6),(24,24),(36,36))
        self.add_polyline('arrow',(6,42),(24,24),(30,18),(42,6))
        self.add_polyline('arrowhead',(30,6),(42,6),(42,18))
        self.add_polyline('fletching',(6,34),(6,42),(14,42))
        for a,b in [('bow','string'),('bow','arrow'),('string','arrow'),('arrow','arrowhead'),('arrow','fletching')]:self.relate('connect',a,b)
