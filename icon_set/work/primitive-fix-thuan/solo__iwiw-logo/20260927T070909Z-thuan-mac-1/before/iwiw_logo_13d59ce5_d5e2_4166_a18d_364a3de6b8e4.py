"""A chunky hexagonal C made of angular outlined strokes with an inner angled line, beside a short vertical bar at the right.

Plan: Angular C with inner angled accent and an independent right bar.
Keyshape: SQUARE; exact SOLO48 envelope from the contract.
Construction reference: Previously inspected hexagon: coherent angular silhouette.
Simplification: Thick outline and right capsule reduce to strokes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '13d59ce5-d5e2-4166-a18d-364a3de6b8e4'
SOURCE_PATH = 'pictographic-primitives/logos/iwiw logo_13d59ce5-d5e2-4166-a18d-364a3de6b8e4.svg'
AUTHOR = 'gpt-6'


class IwiwLogo(Solo48):
    icon_id = 'iwiw-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('iwiw', 'social', 'letter-c', 'logo', 'brand', 'network', 'hungarian')

    def build(self):
        self.add_polyline('C',(32,12),(24,6),(6,18),(6,30),(24,42),(32,36))
        self.add_polyline('inner',(25,20),(18,24),(18,28))
        self.add_line('bar',(42,16),(42,32))
