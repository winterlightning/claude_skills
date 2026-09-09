"""Frontal buffalo: broad brow, rounded jaw, mirrored upturned horns, eyes and muzzle. HRECT_XL (2,5)-(46,43). Removed pinched chin. No useful exact Lucide match."""
# Variant of buffalo-head; parent file remains unchanged.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'dfa6681e-c282-4464-9e3f-8da4256d4f83'
SOURCE_PATH = 'pictographic-primitives/animals/buffalo_dfa6681e-c282-4464-9e3f-8da4256d4f83.svg'
AUTHOR = 'gpt-6'

class BuffaloHeadVariant2(Solo48):
    icon_id = 'buffalo-head-v2'
    variant_of = 'buffalo-head'
    variant_label = 'Broad buffalo face and horns'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/animals'
    aliases = ()
    keywords = ('buffalo', 'bison', 'head', 'horns', 'cattle', 'animal', 'wildlife', 'ox')

    def build(self) -> None:
        # Broad front-facing head with short upturned horns, extremes (2,5)-(46,43).
        self.add_arc('horn-left',(2,5),(13,20),radius_x=11,radius_y=15,sweep=False)
        self.add_line('brow',(13,20),(35,20))
        self.add_arc('horn-right',(35,20),(46,5),radius_x=11,radius_y=15,sweep=False)
        self.add_contour('horns','horn-left','brow','horn-right')
        self.add_line('left-cheek',(13,20),(13,32))
        self.add_arc('left-jaw',(13,32),(24,43),radius_x=11,sweep=False)
        self.add_arc('right-jaw',(24,43),(35,32),radius_x=11,sweep=False)
        self.add_line('right-cheek',(35,32),(35,20))
        self.add_contour('face','left-cheek','left-jaw','right-jaw','right-cheek')
        self.relate('connect','horns','face')
        self.add_dot('eye-left',(20,28))
        self.add_dot('eye-right',(28,28))
        self.add_line('muzzle',(22,35),(26,35))
