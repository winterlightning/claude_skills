"""Three thick rounded corner brackets frame the upper left, upper right and lower left of a central circle. A small separate ring fills the lower right corner.

Plan: Three matching scan corners with radius 8; central radius 6 circle and separate radius 3 ring.
Keyshape: SQUARE; exact SOLO48 envelope from the contract.
Construction reference: scan: quarter-circle corners with shared radius.
Simplification: Double outlines on corner brackets reduce to single strokes; lower-right asymmetry preserved.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b6bfc6b3-7de6-4242-be44-f93a0031cee7'
SOURCE_PATH = 'pictographic-primitives/logos/google lens logo_b6bfc6b3-7de6-4242-be44-f93a0031cee7.svg'
AUTHOR = 'gpt-6'


class GoogleLensLogo(Solo48):
    icon_id = 'google-lens-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('google-lens', 'google', 'camera', 'visual-search', 'logo', 'brand', 'scan')

    def build(self):
        for n,s,e,c in [('tl',(6,18),(18,6),(6,6)),('tr',(30,6),(42,18),(42,6)),('bl',(18,42),(6,30),(6,42))]:
            if n=='tl': pts=((6,18),(6,14),(14,6),(18,6))
            elif n=='tr': pts=((30,6),(34,6),(42,14),(42,18))
            else: pts=((18,42),(14,42),(6,34),(6,30))
            self.add_line(n+'-a',pts[0],pts[1])
            self.add_arc(n+'-turn',pts[1],pts[2],radius_x=8)
            self.add_line(n+'-b',pts[2],pts[3])
            self.add_contour(n,n+'-a',n+'-turn',n+'-b')
        for n,x,y,r in [('lens',24,24,6),('ring',39,39,3)]:
            self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
