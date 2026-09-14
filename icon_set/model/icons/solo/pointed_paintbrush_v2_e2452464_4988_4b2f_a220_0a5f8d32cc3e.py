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
        self.add_line('handle-upper', (20, 24), (36, 8))
        self.add_arc('cap-top', (36, 8), (40, 8), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('cap-right', (40, 8), (40, 12), radius_x=4, radius_y=4, sweep=True)
        self.add_line('handle-lower', (40, 12), (26, 30))
        self.add_line('ferrule', (26, 30), (20, 24))
        self.add_contour('handle', 'handle-upper', 'cap-top', 'cap-right', 'handle-lower', 'ferrule', closed=True)
        self.add_arc('bristle-crown', (20, 24), (8, 32), radius_x=10, radius_y=10, sweep=False)
        self.add_line('bristle-tip', (8, 32), (6, 42))
        self.add_line('bristle-bottom', (6, 42), (22, 42))
        self.add_arc('bristle-side', (22, 42), (26, 30), radius_x=11, radius_y=11, sweep=False)
        self.add_contour('bristles', 'bristle-crown', 'bristle-tip', 'bristle-bottom', 'bristle-side', closed=False)
        self.relate("connect", 'handle', 'bristles')
