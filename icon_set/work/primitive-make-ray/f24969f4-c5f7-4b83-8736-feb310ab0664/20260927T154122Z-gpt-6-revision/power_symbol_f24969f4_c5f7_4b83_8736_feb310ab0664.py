"""Open circular power ring with central stem. Lucide power informs the detached stem and wide top opening.

SOLO48 VRECT_L; geometry authored from its exact centerline extremes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f24969f4-c5f7-4b83-8736-feb310ab0664'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__power-symbol/20260927T153747Z-thuan-mac-1/reference/power_f24969f4-c5f7-4b83-8736-feb310ab0664.svg'
AUTHOR = "gpt-6"

class PowerSymbol(Solo48):
    icon_id = 'power-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol',)
    aliases = ()
    keywords = ('power', 'on-off', 'shutdown', 'switch', 'button', 'standby', 'turn-off', 'energy')

    def build(self) -> None:
        # One open ring and one detached stem, with mirrored shoulders.
        self.add_line('stem', (24, 6), (24, 23))
        self.add_bezier('ring-left', (15, 12), ((10, 16), (6, 21), (6, 26)), ((6, 35), (14, 42), (24, 42)))
        self.add_bezier('ring-right', (24, 42), ((34, 42), (42, 35), (42, 26)), ((42, 21), (38, 16), (33, 12)))
        self.add_contour('ring', 'ring-left', 'ring-right')
