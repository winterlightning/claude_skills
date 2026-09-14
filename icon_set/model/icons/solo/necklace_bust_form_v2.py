# Variant of necklace-bust-form; parent file remains unchanged.
'Mirrored necklace bust with a detached, narrower chain providing wider clear space. VRECT_XL preserves the bust silhouette. No useful Lucide subject match.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '57cd05d6-858f-52cb-9183-c06310d44846'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-03/necklace_57cd05d6-858f-52cb-9183-c06310d44846.svg'
AUTHOR = 'gpt-6'

class NecklaceBustFormVariant2(Solo48):
    icon_id = 'necklace-bust-form-v2'
    variant_of = 'necklace-bust-form'
    variant_label = 'Wider necklace clearance'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('necklace', 'bust', 'form', 'display', 'mannequin', 'jewellery', 'jewelry', 'torso', 'stand')

    def build(self) -> None:
        self.add_line('neck-top', (15, 6), (33, 6))
        self.add_arc('neck-right-top', (33, 6), (37, 10), radius_x=10, radius_y=10, sweep=False)
        self.add_arc('neck-right-bottom', (37, 10), (42, 12), radius_x=10, radius_y=10, sweep=False)
        self.add_line('base-1', (42, 12), (35, 42))
        self.add_line('base-2', (35, 42), (13, 42))
        self.add_line('base-3', (13, 42), (6, 12))
        self.add_arc('neck-left-bottom', (6, 12), (11, 10), radius_x=10, radius_y=10, sweep=False)
        self.add_arc('neck-left-top', (11, 10), (15, 6), radius_x=10, radius_y=10, sweep=False)
        self.add_contour('form', 'neck-top', 'neck-right-top', 'neck-right-bottom', 'base-1', 'base-2', 'base-3', 'neck-left-bottom', 'neck-left-top', closed=True)
        self.add_arc('necklace', (17, 14), (31, 14), radius_x=7, radius_y=13, sweep=False)
