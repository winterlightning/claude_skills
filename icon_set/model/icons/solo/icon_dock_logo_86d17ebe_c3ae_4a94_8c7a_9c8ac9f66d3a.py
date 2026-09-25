"""An anchor with a round ring at its top, a straight shank and two curved arms ending in arrowheads at the lower left and right.

Plan: Ring and vertical shaft meeting a mirrored angular anchor, connected arrow tips.
Keyshape: SQUARE; exact SOLO48 envelope from the contract.
Construction reference: anchor: ring, shaft and physically joined flukes.
Simplification: Detached arrowheads joined to the arms.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '86d17ebe-c3ae-4a94-8c7a-9c8ac9f66d3a'
SOURCE_PATH = 'pictographic-primitives/logos/icon dock logo_86d17ebe-c3ae-4a94-8c7a-9c8ac9f66d3a.svg'
AUTHOR = 'gpt-6'


class IconDockLogo(Solo48):
    icon_id = 'icon-dock-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('icon-dock', 'anchor', 'icons', 'logo', 'brand', 'marketplace', 'design')

    def build(self):
        self.add_arc('r1',(24,6),(24,18),radius_x=6)
        self.add_arc('r2',(24,18),(24,6),radius_x=6)
        self.add_contour('ring','r1','r2',closed=True)
        self.add_line('shaft',(24,18),(24,42))
        self.relate('connect','ring','shaft')
        self.add_polyline('arms',(6,24),(24,42),(42,24))
        self.relate('connect','arms','shaft')
        self.add_polyline('left-tip',(6,32),(6,24),(14,24))
        self.add_polyline('right-tip',(34,24),(42,24),(42,32))
        self.relate('connect','arms','left-tip')
        self.relate('connect','arms','right-tip')
