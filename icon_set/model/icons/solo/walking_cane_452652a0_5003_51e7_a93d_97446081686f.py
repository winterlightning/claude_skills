"""A left-hooked walking cane. VRECT_S extremes (14,2)-(34,46). Lucide candy-cane informs the tangent arc-to-shaft join; the original single stroke is retained. Intentional left hook."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '452652a0-5003-51e7-a93d-97446081686f'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-05/cane_452652a0-5003-51e7-a93d-97446081686f.svg'
AUTHOR = 'astra-chatgpt'


class WalkingCane(Solo48):
    icon_id = 'walking-cane'
    keyshape = Keyshape.VRECT_S
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('cane', 'walking stick', 'crook', 'stick', 'handle', 'accessory', 'mobility', 'hook')

    def build(self) -> None:
        self.add_arc('hook', (14, 12), (34, 12), radius_x=10, radius_y=10, sweep=True)
        self.add_line('shaft', (34, 12), (34, 46))
        self.add_contour('cane', 'hook', 'shaft', closed=False)
