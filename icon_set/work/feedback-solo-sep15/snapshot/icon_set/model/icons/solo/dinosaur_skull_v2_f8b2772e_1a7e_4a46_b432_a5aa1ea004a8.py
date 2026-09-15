"""Increase the mouth separation from 8 to 10 centerline units and align both dot apertures on one height. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f8b2772e-1a7e-4a46-b432-a5aa1ea004a8'
SOURCE_PATH = 'pictographic-primitives/culture/batch-02/dinosaur skull fossil_f8b2772e-1a7e-4a46-b432-a5aa1ea004a8.svg'
AUTHOR = 'gpt-6'

class DinosaurSkullVariant2(Solo48):
    icon_id = 'dinosaur-skull-v2'
    variant_of = 'dinosaur-skull'
    variant_label = 'Increase the mouth separation from 8 to 10 centerline units and align both dot apertures on one height.'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/culture'
    aliases = ()
    keywords = ('dinosaur', 'skull', 'fossil', 'prehistoric', 'palaeontology', 'bone', 'raptor', 'museum')

    def build(self) -> None:
        """Symbol plan: Increase the mouth separation from 8 to 10 centerline units and align both dot apertures on one height. Reference: inspected current parent; no useful exact Lucide match selected."""
        self.add_line('snout-1', (6, 24), (6, 22))
        self.add_line('snout-2', (6, 22), (6, 6))
        self.add_line('snout-3', (6, 6), (30, 6))
        self.add_line('snout-4', (30, 6), (34, 6))
        self.add_arc('braincase', (34, 6), (42, 17), radius_x=12)
        self.add_line('back', (42, 17), (42, 31))
        self.add_arc('jaw-back', (42, 31), (34, 42), radius_x=12)
        self.add_line('jaw-1', (34, 42), (12, 42))
        self.add_line('jaw-2', (12, 42), (6, 34))
        self.add_line('jaw-3', (6, 34), (29, 34))
        self.add_line('jaw-4', (29, 34), (36, 24))
        self.add_line('jaw-5', (36, 24), (6, 24))
        self.add_contour('skull', 'snout-1', 'snout-2', 'snout-3', 'snout-4', 'braincase', 'back', 'jaw-back', 'jaw-1', 'jaw-2', 'jaw-3', 'jaw-4', 'jaw-5', closed=True)
        self.add_dot('eye', (31, 15))
        self.add_dot('nostril', (15, 15))
