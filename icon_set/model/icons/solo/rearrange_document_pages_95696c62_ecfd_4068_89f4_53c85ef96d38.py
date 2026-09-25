"""Rearrange Document Pages. Reference retains the complete subject following saved user classification.
Plan: HRECT_L envelope; shared page/currency dimensions and true beam attachment nodes.
Lucide files informs page contour continuity; dollar-sign informs paired currency bowls.
Source supplies count, relative placement and intentional asymmetry. Decorative thickness omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '95696c62-ecfd-4068-89f4-53c85ef96d38'
SOURCE_PATH = 'pictographic-primitives/files/reorder pdf pages_95696c62-ecfd-4068-89f4-53c85ef96d38.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'rearrange-document-pages'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'files'
    categories = ('files', 'primitives')
    aliases = ()
    keywords = ('rearrange', 'document', 'pages')

    def build(self):

        def rect(name,l,t,r,b):
            self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),closed=True)

        for j,x in enumerate((4,20,36)):
            rect('page-'+str(j),x,24,x+8,40)
        self.add_bezier('arrow-left',(12,16),((12,11),(18,8),(24,8)))
        self.add_bezier('arrow-right',(24,8),((30,8),(34,11),(36,16)))
        self.add_contour('arrow-curve','arrow-left','arrow-right')
        self.add_polyline('arrowhead',(28,16),(36,16),(36,8))
        self.relate('connect','arrow-curve','arrowhead')
