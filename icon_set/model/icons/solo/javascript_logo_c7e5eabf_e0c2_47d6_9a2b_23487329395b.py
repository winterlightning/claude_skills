"""A rounded square frame holds the letters JS in its lower right corner.

Plan: Wide brand tile provides room for J and S in the lower field.
Keyshape: HRECT_L; exact SOLO48 envelope from the contract.
Construction reference: Previously inspected file-text: sparse letter-like detail in tile.
Simplification: Tile widened and letters enlarged for native-size clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c7e5eabf-e0c2-47d6-9a2b-23487329395b'
SOURCE_PATH = 'pictographic-primitives/logos/java script logo_c7e5eabf-e0c2-47d6-9a2b-23487329395b.svg'
AUTHOR = 'gpt-6'


class JavascriptLogo(Solo48):
    icon_id = 'javascript-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('javascript', 'js', 'programming', 'language', 'logo', 'brand', 'web')

    def build(self):
        self.add_polyline('frame',(4,8),(44,8),(44,40),(4,40),closed=True)
        self.add_line('jt',(20,17),(20,27))
        self.add_bezier('jb',(20,27),((20,33),(13,33),(13,27)))
        self.add_contour('J','jt','jb')
        self.add_bezier('S',(35,18),((29,14),(29,19),(29,21)),((29,24),(35,24),(35,28)),((35,33),(29,33),(29,29)))
