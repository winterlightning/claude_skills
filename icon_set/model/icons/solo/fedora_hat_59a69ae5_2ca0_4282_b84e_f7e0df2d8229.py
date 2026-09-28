"""Fedora with central crease, tapered crown and hatband. HRECT_L extremes (4,8)-(44,40). Lucide hat-glasses informs crease and flared crown; intentional crease corners retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '59a69ae5-2ca0-4282-b84e-f7e0df2d8229'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-03/hat_59a69ae5-2ca0-4282-b84e-f7e0df2d8229.svg'
AUTHOR = 'gpt-6'


class FedoraHat(Solo48):
    icon_id = 'fedora-hat'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "accessories"
    categories = ("primitives", "accessories")
    aliases = ()
    keywords = ('hat', 'fedora', 'trilby', 'brim', 'formal', 'vintage', 'headwear', 'crease')

    def build(self) -> None:
        self.add_line('crown-1', (8, 40), (10, 24))
        self.add_line('crown-2', (10, 24), (12, 8))
        self.add_line('crown-3', (12, 8), (24, 15))
        self.add_line('crown-4', (24, 15), (36, 8))
        self.add_line('crown-5', (36, 8), (38, 24))
        self.add_line('crown-6', (38, 24), (40, 40))
        self.add_contour('crown', 'crown-1', 'crown-2', 'crown-3', 'crown-4', 'crown-5', 'crown-6', closed=False)
        self.add_line('brim-attach-0', (4, 40), (8, 40))
        self.add_line('brim-attach-1', (8, 40), (40, 40))
        self.add_line('brim-attach-2', (40, 40), (44, 40))
        self.add_contour('brim', 'brim-attach-0', 'brim-attach-1', 'brim-attach-2')
        self.add_line('band', (10, 24), (38, 24))
        self.relate("connect", 'crown', 'brim')
        self.relate("connect", 'crown', 'band')
