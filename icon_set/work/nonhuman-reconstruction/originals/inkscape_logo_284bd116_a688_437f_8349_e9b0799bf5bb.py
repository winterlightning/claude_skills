"""A diamond-topped mountain with a jagged snow line near its peak melts into dripping wavy layers that narrow to a rounded base.

Plan: Symmetric mountain peak and broad ink-drop base, attached snow zigzag.
Keyshape: SQUARE; exact SOLO48 envelope from the contract.
Construction reference: mountain: deliberate angular summit; flower-2: coherent rounded contour.
Simplification: Multiple ink ripples reduce to one broad flowing drop.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '284bd116-a688-437f-8349-e9b0799bf5bb'
SOURCE_PATH = 'pictographic-primitives/logos/inkscape logo_284bd116-a688-437f-8349-e9b0799bf5bb.svg'
AUTHOR = 'gpt-6'


class InkscapeLogo(Solo48):
    icon_id = 'inkscape-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('inkscape', 'vector', 'drawing', 'logo', 'brand', 'open-source', 'mountain')

    def build(self):
        self.add_polyline('peak',(6,24),(12,18),(24,6),(36,18),(42,24))
        self.add_bezier('base',(42,24),((42,32),(30,30),(30,36)),((30,40),(32,42),(24,42)),((16,42),(18,40),(18,36)),((18,30),(6,32),(6,24)))
        self.relate('connect','peak','base')
        self.add_polyline('snow',(6,24),(16,25),(24,18),(32,25),(42,24))
        self.relate('connect','snow','peak')
