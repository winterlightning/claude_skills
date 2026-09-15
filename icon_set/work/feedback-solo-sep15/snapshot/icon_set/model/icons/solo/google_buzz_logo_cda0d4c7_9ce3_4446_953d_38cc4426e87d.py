"""An oval speech bubble with a pointed tail at the lower left is crossed by two diagonal strokes, one extending beyond its upper right edge.

Plan: Oval speech bubble and two diagonal runs with shared integer crossing nodes.
Keyshape: SQUARE; exact SOLO48 envelope from the contract.
Construction reference: message-circle: bubble contour; no exact brand match.
Simplification: Colour omitted; diagonal motif and lower-left tail retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cda0d4c7-9ce3-4446-953d-38cc4426e87d'
SOURCE_PATH = 'pictographic-primitives/logos/google buzz logo_cda0d4c7-9ce3-4446-953d-38cc4426e87d.svg'
AUTHOR = 'gpt-6'


class GoogleBuzzLogo(Solo48):
    icon_id = 'google-buzz-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('google-buzz', 'google', 'social', 'speech-bubble', 'logo', 'brand', 'chat')

    def build(self):
        # Every diagonal crossing is an explicit shared integer node.
        self.add_bezier('upper-left',(6,24),((6,18),(8,16),(12,12)),((16,8),(20,6),(24,6)))
        self.add_bezier('upper-right',(24,6),((28,6),(31,8),(34,12)),((38,17),(42,18),(42,24)))
        self.add_bezier('lower-right',(42,24),((42,29),(40,31),(36,34)),((31,37),(25,36),(19,36)))
        self.add_line('tail-1',(19,36),(9,42))
        self.add_line('tail-2',(9,42),(12,32))
        self.add_bezier('lower-left',(12,32),((8,30),(6,27),(6,24)))
        self.add_contour('outline','upper-left','upper-right','lower-right','tail-1','tail-2','lower-left',closed=True)
        self.add_polyline('slash',(9,42),(24,24),(34,12),(39,6))
        self.add_polyline('stripe',(12,12),(24,24),(36,34))
        self.relate('connect','outline','slash')
        self.relate('connect','outline','stripe')
        self.relate('connect','slash','stripe')
