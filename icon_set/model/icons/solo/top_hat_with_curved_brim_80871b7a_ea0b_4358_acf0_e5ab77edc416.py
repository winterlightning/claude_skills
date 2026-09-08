"""A tall top hat with a broad curved brim and band; simplify the brim dip into a smooth bowl.

Lucide construction: hat-glasses: minimal crown above a wide brim.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '80871b7a-ea0b-4358-acf0-e5ab77edc416'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-02/hat 1_80871b7a-ea0b-4358-acf0-e5ab77edc416.svg'
AUTHOR = 'astra-chatgpt'


class TopHatWithCurvedBrim(Solo48):
    icon_id = 'top-hat-with-curved-brim'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('hat', 'top hat', 'formal', 'brim', 'gentleman', 'magic', 'headwear', 'vintage')

    def build(self) -> None:
        # Exact keyshape envelope: (0, 3, 48, 45).
        self.add_line('crown-left-1', (12, 32), (12, 24))
        self.add_line('crown-left-2', (12, 24), (10, 9))
        self.add_arc('crown-tl', (10, 9), (14, 5), radius_x=4, radius_y=4, sweep=True)
        self.add_line('crown-top', (14, 5), (34, 5))
        self.add_arc('crown-tr', (34, 5), (38, 9), radius_x=4, radius_y=4, sweep=True)
        self.add_line('crown-right-1', (38, 9), (36, 24))
        self.add_line('crown-right-2', (36, 24), (36, 32))
        self.add_contour('crown', 'crown-left-1', 'crown-left-2', 'crown-tl', 'crown-top', 'crown-tr', 'crown-right-1', 'crown-right-2', closed=False)
        self.add_line('band', (12, 24), (36, 24))
        self.add_line('brim-top-1', (2, 32), (12, 32))
        self.add_line('brim-top-2', (12, 32), (36, 32))
        self.add_line('brim-top-3', (36, 32), (46, 32))
        self.add_arc('brim-right', (46, 32), (24, 43), radius_x=22, radius_y=11, sweep=True)
        self.add_arc('brim-left', (24, 43), (2, 32), radius_x=22, radius_y=11, sweep=True)
        self.add_contour('brim', 'brim-top-1', 'brim-top-2', 'brim-top-3', 'brim-right', 'brim-left', closed=True)
        self.relate("connect", 'crown', 'band')
        self.relate("connect", 'crown', 'brim')
