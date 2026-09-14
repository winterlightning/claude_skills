# Variant of pointed-paintbrush; parent file remains unchanged.
"""A diagonal paintbrush with a rounded handle and a broad pointed bristle head."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e2452464-4988-4b2f-a220-0a5f8d32cc3e'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-01/brush_e2452464-4988-4b2f-a220-0a5f8d32cc3e.svg'
AUTHOR = 'gpt-6'

class PointedPaintbrushVariant2(Solo48):
    icon_id = 'pointed-paintbrush-v2'
    variant_of = 'pointed-paintbrush'
    variant_label = 'Design rules: exact bounds and open spacing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/decoration'
    aliases = ()
    keywords = ('paintbrush', 'brush', 'paint', 'art', 'bristles', 'handle', 'craft')

    def build(self):
        # Lucide paintbrush: diagonal handle and broad bristle head. Intentional bristle point; coherent cap will be checked against exact square extrema.
        self.add_line('handle-upper', (18, 19), (34, 7))
        self.add_arc('cap', (34, 7), (40, 15), radius_x=5, radius_y=5, sweep=True)
        self.add_line('handle-lower', (40, 15), (24, 27))
        self.add_line('ferrule', (24, 27), (18, 19))
        self.add_contour('handle', 'handle-upper', 'cap', 'handle-lower', 'ferrule', closed=True)
        self.add_arc('bristle-crown', (18, 19), (8, 32), radius_x=14, radius_y=14, sweep=False)
        self.add_line('bristle-tip', (8, 32), (6, 42))
        self.add_line('bristle-bottom', (6, 42), (22, 42))
        self.add_arc('bristle-side', (22, 42), (24, 27), radius_x=16, radius_y=16, sweep=False)
        self.add_contour('bristles', 'bristle-crown', 'bristle-tip', 'bristle-bottom', 'bristle-side', closed=False)
        self.relate("connect", 'handle', 'bristles')
