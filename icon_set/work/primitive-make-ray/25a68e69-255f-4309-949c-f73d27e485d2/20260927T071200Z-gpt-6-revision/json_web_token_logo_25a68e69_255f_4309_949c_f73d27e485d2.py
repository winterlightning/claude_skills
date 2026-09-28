"""An eight-armed starburst drawn as a single outline, with thick straight arms radiating from an open centre.

Plan: Eight equally directed arms share a central junction.
Keyshape: SQUARE; exact SOLO48 envelope from the contract.
Construction reference: asterisk: radial joined strokes.
Simplification: Outlined arms merge into a monoline eight-arm burst.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '25a68e69-255f-4309-949c-f73d27e485d2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__json-web-token-logo/20260927T070927Z-thuan-mac-1/reference/json web token logo_25a68e69-255f-4309-949c-f73d27e485d2.svg'
AUTHOR = 'gpt-6'


class JsonWebTokenLogo(Solo48):
    icon_id = 'json-web-token-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('jwt', 'json-web-token', 'authentication', 'starburst', 'logo', 'brand', 'security')

    def build(self):
        # One notched contour gives the source's eight broad, flat-ended rays.
        from math import cos, sin, pi
        points=[]
        for i in range(8):
            angle=-pi/2+i*pi/4
            cx,cy=24+18*cos(angle),24+18*sin(angle)
            tx,ty=-sin(angle),cos(angle)
            points.append((round(cx-5*tx),round(cy-5*ty)))
            points.append((round(cx+5*tx),round(cy+5*ty)))
            mid=angle+pi/8
            points.append((round(24+10*cos(mid)),round(24+10*sin(mid))))
        self.add_polyline('burst',*points,closed=True)
