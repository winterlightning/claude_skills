# Variant of flying-bird; parent file remains unchanged.
'Flying bird with a single raised wing, rounded breast and simple beak. SQUARE (2,2)-(46,46) retains flight height. Feather zigzags removed. Lucide bird informed broad contours. Deliberate right-facing asymmetry.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '00732191-23f0-53ae-84da-b288489181c6'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird fly_00732191-23f0-53ae-84da-b288489181c6.svg'
AUTHOR = 'gpt-6'

class FlyingBirdVariant2(Solo48):
    icon_id = 'flying-bird-v2'
    variant_of = 'flying-bird'
    variant_label = 'Simple raised wing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('bird', 'flying', 'wings', 'dove', 'flight', 'sky', 'freedom', 'soar')

    def build(self) -> None:
        self.add_line('wing-1', (8,35), (2,2))
        self.add_line('wing-6', (2,2), (23,18))
        self.add_arc('wing-fold', (23, 18), (25, 27), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('throat', (25, 27), (31, 25), radius_x=3, radius_y=5, sweep=False)
        self.add_line('neck', (31, 25), (31, 18))
        self.add_arc('head', (31, 18), (43, 18), radius_x=6, radius_y=8, sweep=True)
        self.add_line('beak-1', (43, 18), (46, 24))
        self.add_line('beak-2', (46, 24), (43, 26))
        self.add_line('breast-top', (43, 26), (43, 28))
        self.add_arc('breast', (43, 28), (25, 46), radius_x=18, radius_y=18, sweep=True)
        self.add_arc('tail', (25, 46), (8, 35), radius_x=20, radius_y=20, sweep=True)
        self.add_contour('body', 'wing-1', 'wing-6', 'wing-fold', 'throat', 'neck', 'head', 'beak-1', 'beak-2', 'breast-top', 'breast', 'tail', closed=True)
