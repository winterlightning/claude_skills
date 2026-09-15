"""Enlarge the forked tail and projecting pectoral fin, preserving a broad curved back and a clear inner belly. Independent feedback revision; parent preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c0fe22a4-31db-554f-b6d7-6ce3be390288'
SOURCE_PATH = 'pictographic-primitives/animals/dolphin_c0fe22a4-31db-554f-b6d7-6ce3be390288.svg'
AUTHOR = 'gpt-6'

class LeapingDolphinVariant2(Solo48):
    icon_id = 'leaping-dolphin-v2'
    variant_of = 'leaping-dolphin'
    variant_label = 'Enlarge the forked tail and projecting pectoral fin, preserving a broad curved back and a clear inner belly.'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('dolphin', 'leap', 'jump', 'sea', 'marine', 'ocean', 'mammal', 'swim')

    def build(self) -> None:
        """Symbol plan: Enlarge the forked tail and projecting pectoral fin, preserving a broad curved back and a clear inner belly. Reference: Lucide fish: angular fins attached to a coherent curved body."""
        self.add_bezier('back-low', (6, 32), ((6, 20), (10, 8), (20, 8)))
        self.add_line('dorsal-rise', (20, 8), (25, 6))
        self.add_bezier('back-high', (25, 6), ((32, 6), (42, 16), (42, 24)))
        self.add_line('nose', (42, 24), (33, 20))
        self.add_bezier('chin', (33, 20), ((31, 22), (29, 24), (25, 24)))
        self.add_line('flipper', (25, 24), (30, 14))
        self.add_bezier('belly', (30, 14), ((18, 16), (16, 24), (16, 32)))
        self.add_line('tail-inner', (16, 32), (32, 42))
        self.add_line('tail-tip', (32, 42), (18, 38))
        self.add_line('tail-notch', (18, 38), (6, 42))
        self.add_line('tail-back', (6, 42), (6, 32))
        self.add_contour('outline', 'back-low', 'dorsal-rise', 'back-high', 'nose', 'chin', 'flipper', 'belly', 'tail-inner', 'tail-tip', 'tail-notch', 'tail-back', closed=True)
