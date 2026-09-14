"""Open circular power ring with central stem. Lucide power informs the detached stem and wide top opening.

SOLO48 VRECT_L; geometry authored from its exact centerline extremes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f24969f4-c5f7-4b83-8736-feb310ab0664'
SOURCE_PATH = 'pictographic-primitives/symbol/power_f24969f4-c5f7-4b83-8736-feb310ab0664.svg'
AUTHOR = 'gpt-6'


class PowerSymbol(Solo48):
    icon_id = 'power-symbol'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('power', 'on-off', 'shutdown', 'switch', 'button', 'standby', 'turn-off', 'energy')

    def build(self) -> None:

        self.add_line('stem', (24,6), (24,24))
        self.add_arc('ring-left', (14,12), (8,28), radius_x=6, radius_y=16, sweep=False)
        self.add_arc('ring-bottom', (8,28), (40,28), radius_x=16, sweep=False)
        self.add_arc('ring-right', (40,28), (34,12), radius_x=6, radius_y=16, sweep=False)
        self.add_contour('ring', 'ring-left', 'ring-bottom', 'ring-right')
