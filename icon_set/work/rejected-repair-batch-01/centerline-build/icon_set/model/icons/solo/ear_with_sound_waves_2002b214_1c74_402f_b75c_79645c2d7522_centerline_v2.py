"""Smooth the ear’s long descending wall into the lobe with a single tangent curve; the outline no longer has a sudden bend at the lower ear.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2002b214-1c74-402f-b75c-79645c2d7522'
SOURCE_PATH = 'pictographic-primitives/wayfinding/disability hearing_2002b214-1c74-402f-b75c-79645c2d7522.svg'
AUTHOR = 'gpt-6'

class EarWithSoundWaves(Solo48):
    icon_id = 'ear-with-sound-waves-centerline-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('ear', 'hearing', 'sound', 'audio', 'listening', 'accessibility')

    def build(self):
        self.add_arc('ear-top', (6, 26), (22, 26), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_bezier('ear-down', (22, 26), ((22, 31), (18, 31), (18, 36)))
        self.add_arc('ear-lobe', (18, 36), (6, 36), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('wave-inner', (29, 15), (33, 19), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_arc('wave-outer', (29, 6), (42, 19), radius_x=13, radius_y=13, large_arc=False, sweep=True)
        self.add_contour('ear', 'ear-top', 'ear-down', 'ear-lobe', closed=False)
    variant_of = 'ear-with-sound-waves'
    variant_label = 'Batch 01 centerline repair'
