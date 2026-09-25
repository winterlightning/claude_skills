"""A pitched-roof garage has a wide open door and one shutter slat. HRECT_L extremes (6,8)-(42,40). Lucide warehouse informs roof symmetry, wall jambs and horizontal slats; retain one source slat with a wider opening."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '94ec5fe1-843b-4e2e-9864-b900350953aa'
SOURCE_PATH = 'pictographic-primitives/symbol/garage_94ec5fe1-843b-4e2e-9864-b900350953aa.svg'
AUTHOR = 'gpt-6'


class Garage(Solo48):
    icon_id = 'garage'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol", "state")
    aliases = ()
    keywords = ('garage', 'warehouse', 'building', 'parking', 'car', 'storage', 'depot', 'door')

    def build(self) -> None:
        self.add_polyline('building', (4,40),(4,15),(24,8),(44,15),(44,40),(34,40),(34,32),(34,24),(14,24),(14,32),(14,40),(4,40))
        self.add_line('door-slat', (14,32),(34,32))
        self.relate('connect', 'building','door-slat')
