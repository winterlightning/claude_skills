"""A sombrero with a narrow domed crown and very wide upturned brim; omit straw texture.

Lucide construction: hat-glasses: broad brim and a simple crown.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1c8abf37-4cc4-54b0-8d99-9072a76c457d'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-02/hat sombrero_1c8abf37-4cc4-54b0-8d99-9072a76c457d.svg'
AUTHOR = 'astra-chatgpt'


class Sombrero(Solo48):
    icon_id = 'sombrero'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('hat', 'sombrero', 'mexican', 'wide brim', 'sun hat', 'fiesta', 'headwear', 'straw')

    def build(self) -> None:
        # Exact keyshape envelope: (0, 6, 48, 42).
        self.add_arc('crown-top', (18, 14), (30, 14), radius_x=6, radius_y=6, sweep=True)
        self.add_line('crown-left', (13, 30), (18, 14))
        self.add_line('crown-right', (30, 14), (35, 30))
        self.add_contour('crown', 'crown-left', 'crown-top', 'crown-right', closed=False)
        self.add_line('brim-top-1', (2, 30), (13, 30))
        self.add_line('brim-top-2', (13, 30), (35, 30))
        self.add_line('brim-top-3', (35, 30), (46, 30))
        self.add_arc('brim-right', (46, 30), (34, 40), radius_x=12, radius_y=10, sweep=True)
        self.add_line('brim-base', (34, 40), (14, 40))
        self.add_arc('brim-left', (14, 40), (2, 30), radius_x=12, radius_y=10, sweep=True)
        self.add_contour('brim', 'brim-top-1', 'brim-top-2', 'brim-top-3', 'brim-right', 'brim-base', 'brim-left', closed=True)
        self.relate("connect", 'crown', 'brim')
