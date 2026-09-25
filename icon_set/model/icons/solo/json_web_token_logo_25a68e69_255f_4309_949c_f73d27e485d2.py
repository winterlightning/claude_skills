"""An eight-armed starburst drawn as a single outline, with thick straight arms radiating from an open centre.

Plan: Eight equally directed arms share a central junction.
Keyshape: SQUARE; exact SOLO48 envelope from the contract.
Construction reference: asterisk: radial joined strokes.
Simplification: Outlined arms merge into a monoline eight-arm burst.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '25a68e69-255f-4309-949c-f73d27e485d2'
SOURCE_PATH = 'pictographic-primitives/logos/json web token logo_25a68e69-255f-4309-949c-f73d27e485d2.svg'
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
        ends=[(24,6),(37,11),(42,24),(37,37),(24,42),(11,37),(6,24),(11,11)]
        for i,p in enumerate(ends):self.add_line(f'arm{i}',(24,24),p)
        for i in range(8):
         for j in range(i):self.relate('connect',f'arm{i}',f'arm{j}')
