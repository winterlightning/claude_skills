# Variant of dinosaur-skull; parent file remains unchanged.
'Wider open jaw. Independent feedback revision; preserve source subject.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f8b2772e-1a7e-4a46-b432-a5aa1ea004a8'
SOURCE_PATH = 'pictographic-primitives/culture/batch-02/dinosaur skull fossil_f8b2772e-1a7e-4a46-b432-a5aa1ea004a8.svg'
AUTHOR = 'gpt-6'

class DinosaurSkullVariant2(Solo48):
    icon_id = 'dinosaur-skull-v2'
    variant_of = 'dinosaur-skull'
    variant_label = 'Wider open jaw'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/culture'
    aliases = ()
    keywords = ('dinosaur', 'skull', 'fossil', 'prehistoric', 'palaeontology', 'bone', 'raptor', 'museum')

    def build(self) -> None:
        self.add_line('snout-1', (2, 28), (2, 22))
        self.add_line('snout-2', (2, 22), (6, 12))
        self.add_line('snout-3', (6, 12), (30, 5))
        self.add_line('snout-4', (30, 5), (34, 5))
        self.add_arc('braincase', (34, 5), (46, 17), radius_x=12)
        self.add_line('back', (46, 17), (46, 31))
        self.add_arc('jaw-back', (46, 31), (34, 43), radius_x=12)
        self.add_line('jaw-1', (34, 43), (12, 43))
        self.add_line('jaw-2', (12, 43), (6, 37))
        self.add_line('jaw-3', (6, 37), (29, 37))
        self.add_line('jaw-4', (29, 37), (36, 28))
        self.add_line('jaw-5', (36, 28), (2, 28))
        self.add_contour('skull', 'snout-1', 'snout-2', 'snout-3', 'snout-4', 'braincase', 'back', 'jaw-back', 'jaw-1', 'jaw-2', 'jaw-3', 'jaw-4', 'jaw-5', closed=True)
        self.add_arc('eye-top', (31, 18), (37, 18), radius_x=3, sweep=True)
        self.add_arc('eye-bottom', (37, 18), (31, 18), radius_x=3, sweep=True)
        self.add_contour('eye', 'eye-top', 'eye-bottom', closed=True)
        self.add_dot('nostril', (13, 20))
