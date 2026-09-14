"""A flared flashlight with lens band and central switch; bottom cap merged into handle."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f3222e0d-487b-455b-99e6-6d80c4265af2'
SOURCE_PATH = 'pictographic-primitives/tools/flash light_f3222e0d-487b-455b-99e6-6d80c4265af2.svg'
AUTHOR = 'gpt-6'

class UprightFlashlightVariant2(Solo48):
    icon_id = 'upright-flashlight-v2'
    variant_of = 'upright-flashlight'
    variant_label = 'Height envelope and full spacing repair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/tools'
    aliases = ()
    keywords = ('flashlight', 'torch', 'light', 'lamp', 'battery', 'handheld', 'portable', 'tool')

    def build(self) -> None:
        self.add_polyline('outline', (8, 4), (40, 4), (40, 14), (33, 22), (33, 40), (29, 44), (19, 44), (15, 40), (15, 22), (8, 14), closed=True)
        self.add_line('lens', (8, 14), (40, 14))
        self.relate('connect', 'outline', 'lens')
        self.add_line('switch', (24, 28), (24, 32))
