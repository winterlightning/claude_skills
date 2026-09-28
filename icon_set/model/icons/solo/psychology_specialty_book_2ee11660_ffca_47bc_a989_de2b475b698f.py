"""Psychology Specialty Book. Reference retains the complete subject following saved user classification.
Plan: SQUARE envelope; shared page/currency dimensions and true beam attachment nodes.
Lucide files informs page contour continuity; dollar-sign informs paired currency bowls.
Source supplies count, relative placement and intentional asymmetry. Decorative thickness omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2ee11660-ffca-47bc-a989-de2b475b698f'
SOURCE_PATH = 'pictographic-primitives/health/specialty_2ee11660-ffca-47bc-a989-de2b475b698f.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'psychology-specialty-book'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'health'
    categories = ('health', 'primitives')
    aliases = ()
    keywords = ('psychology', 'specialty', 'book')

    def build(self):

        def rect(name,l,t,r,b):
            self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),closed=True)

        # Omit the redundant medallion ring so the psychology symbol remains legible.
        self.add_polyline('book',(6,34),(14,34),(42,34),(42,42),(14,42),(6,42),closed=True)
        self.add_line('binding',(14,34),(14,42))
        self.relate('connect','book','binding')
        self.add_polyline('psi-stem',(24,6),(24,18),(24,26))
        self.add_bezier('psi-left',(16,8),((16,14),(18,18),(24,18)))
        self.add_bezier('psi-right',(24,18),((30,18),(32,14),(32,8)))
        self.add_contour('psi-bowl','psi-left','psi-right')
        self.add_polyline('psi-foot',(20,26),(24,26),(28,26))
        self.relate('connect','psi-stem','psi-bowl')
        self.relate('connect','psi-stem','psi-foot')
