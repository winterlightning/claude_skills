"""Open restart ring with a separate northwest arrow. Lucide rotate-ccw informs coherent ring arcs; source arrow direction preserved.

SOLO48 SQUARE; geometry authored from its exact centerline extremes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '958c6ea9-a7de-42bf-ba04-e08a99041318'
SOURCE_PATH = 'pictographic-primitives/symbol/power off_958c6ea9-a7de-42bf-ba04-e08a99041318.svg'
AUTHOR = 'gpt-6'


class ArrowRestart(Solo48):
    icon_id = 'arrow-restart'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('restart', 'reset', 'reload', 'refresh', 'rotate', 'power', 'undo', 'arrow')

    def build(self) -> None:

        self.add_arc('ring-upper', (24,6), (42,24), radius_x=18)
        self.add_arc('ring-lower', (42,24), (6,24), radius_x=18)
        self.add_contour('ring', 'ring-upper', 'ring-lower')
        self.add_polyline('arrow-head', (6,15), (6,6), (15,6))
        self.add_line('arrow-shaft', (6,6), (20,20))
        self.relate('connect', 'arrow-head', 'arrow-shaft')
