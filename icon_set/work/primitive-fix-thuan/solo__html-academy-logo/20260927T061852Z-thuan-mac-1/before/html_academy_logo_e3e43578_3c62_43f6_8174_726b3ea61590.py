"""A shield-like hexagon holds a tilted isometric slab with two short parallel strokes on its top face.

Plan: Hexagonal shield with an isometric slab, whose left and right nodes attach to the shield.
Keyshape: SQUARE; exact SOLO48 envelope from the contract.
Construction reference: hexagon: symmetric perimeter; shared isometric vertices.
Simplification: Two short top-face strokes omitted to keep faces open.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e3e43578-3c62-43f6-8174-726b3ea61590'
SOURCE_PATH = 'pictographic-primitives/logos/html academy logo_e3e43578-3c62-43f6-8174-726b3ea61590.svg'
AUTHOR = 'gpt-6'


class HtmlAcademyLogo(Solo48):
    icon_id = 'html-academy-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('html-academy', 'education', 'coding', 'logo', 'brand', 'web', 'course')

    def build(self):
        self.add_polyline('shield',(24,6),(42,10),(42,24),(42,33),(24,42),(6,33),(6,24),(6,10),closed=True)
        self.add_polyline('slab',(6,24),(24,16),(42,24),(24,32),closed=True)
        self.add_line('spine',(24,32),(24,42))
        self.relate('connect','shield','slab')
        self.relate('connect','shield','spine')
        self.relate('connect','slab','spine')
