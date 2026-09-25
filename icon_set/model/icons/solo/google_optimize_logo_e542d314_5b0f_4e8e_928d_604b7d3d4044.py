"""Two thick rounded L-shaped strokes nest diagonally, each bending down at its right end like an arrow pointing to the lower left.

Plan: Two nested rounded L bands share 8-unit width, 4-unit end radius and elbow radius.
Keyshape: SQUARE; exact SOLO48 envelope from the contract.
Construction reference: corner-down-right: shared elbow construction.
Simplification: Arrow-like L bands preserved without added arrowheads.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e542d314-5b0f-4e8e-928d-604b7d3d4044'
SOURCE_PATH = 'pictographic-primitives/logos/google optimize logo_e542d314-5b0f-4e8e-928d-604b7d3d4044.svg'
AUTHOR = 'gpt-6'


class GoogleOptimizeLogo(Solo48):
    icon_id = 'google-optimize-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('google-optimize', 'google', 'testing', 'logo', 'brand', 'marketing', 'experiment')

    def build(self):
        for n,x,y in [('upper',20,6),('lower',10,24)]:
            end=x+18 if n=='upper' else x+12
            bottom=y+16 if n=='upper' else y+14
            self.add_line(n+'-top',(x,y),(end,y))
            self.add_arc(n+'-corner',(end,y),(end+4,y+4),radius_x=4)
            self.add_line(n+'-right',(end+4,y+4),(end+4,bottom))
            self.add_arc(n+'-cap',(end+4,bottom),(end-4,bottom),radius_x=4)
            self.add_line(n+'-inside',(end-4,bottom),(end-4,y+8))
            self.add_line(n+'-bottom',(end-4,y+8),(x,y+8))
            self.add_arc(n+'-left',(x,y+8),(x,y),radius_x=4)
            self.add_contour(n,*(n+'-'+s for s in ('top','corner','right','cap','inside','bottom','left')),closed=True)
