"""Fedora with central crease, tapered crown and hatband. HRECT_M extremes (2,11)-(46,37). Lucide hat-glasses informs crease and flared crown; intentional crease corners retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '59a69ae5-2ca0-4282-b84e-f7e0df2d8229'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-03/hat_59a69ae5-2ca0-4282-b84e-f7e0df2d8229.svg'
AUTHOR = 'astra-chatgpt'


class FedoraHat(Solo48):
    icon_id = 'fedora-hat'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('hat', 'fedora', 'trilby', 'brim', 'formal', 'vintage', 'headwear', 'crease')

    def build(self) -> None:
        self.add_line('crown-1', (8, 37), (10, 24))
        self.add_line('crown-2', (10, 24), (12, 11))
        self.add_line('crown-3', (12, 11), (24, 15))
        self.add_line('crown-4', (24, 15), (36, 11))
        self.add_line('crown-5', (36, 11), (38, 24))
        self.add_line('crown-6', (38, 24), (40, 37))
        self.add_contour('crown', 'crown-1', 'crown-2', 'crown-3', 'crown-4', 'crown-5', 'crown-6', closed=False)
        self.add_line('brim-attach-0', (2, 37), (8, 37))
        self.add_line('brim-attach-1', (8, 37), (40, 37))
        self.add_line('brim-attach-2', (40, 37), (46, 37))
        self.add_contour('brim', 'brim-attach-0', 'brim-attach-1', 'brim-attach-2')
        self.add_line('band', (10, 24), (38, 24))
        self.relate("connect", 'crown', 'brim')
        self.relate("connect", 'crown', 'band')
