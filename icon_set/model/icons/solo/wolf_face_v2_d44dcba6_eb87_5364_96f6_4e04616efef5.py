# Variant of wolf-face; parent file remains unchanged.
"""A mirrored wolf face with pointed ears, flared cheeks and a rounded nose."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd44dcba6-eb87-5364-96f6-4e04616efef5'
SOURCE_PATH = 'pictographic-primitives/animals/wolf_d44dcba6-eb87-5364-96f6-4e04616efef5.svg'
AUTHOR = 'gpt-6'

class WolfFaceVariant2(Solo48):
    icon_id = 'wolf-face-v2'
    variant_of = 'wolf-face'
    variant_label = 'Design rules: exact bounds and open spacing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/animals'
    aliases = ('wolf-head',)
    keywords = ('wolf', 'face', 'head', 'ears', 'front', 'muzzle', 'canine', 'wild')

    def build(self):
        # Lucide dog: simple face and centered muzzle; pointed ears preserve wolf identity. Mirror x=24; chin radius 10 reaches y=42 exactly.
        self.add_line('upper-1', (6, 28), (7, 18))
        self.add_line('upper-2', (7, 18), (6, 6))
        self.add_line('upper-3', (6, 6), (16, 10))
        self.add_line('upper-4', (16, 10), (32, 10))
        self.add_line('upper-5', (32, 10), (42, 6))
        self.add_line('upper-6', (42, 6), (41, 18))
        self.add_line('upper-7', (41, 18), (42, 28))
        self.add_line('upper-8', (42, 28), (30, 40))
        self.add_arc('chin', (30, 40), (18, 40), radius_x=10, radius_y=10, sweep=True)
        self.add_line('left-jaw', (18, 40), (6, 28))
        self.add_contour('head', 'upper-1', 'upper-2', 'upper-3', 'upper-4', 'upper-5', 'upper-6', 'upper-7', 'upper-8', 'chin', 'left-jaw', closed=True)
        self.add_arc('nose-a', (21, 30), (27, 30), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('nose-b', (27, 30), (21, 30), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('nose', 'nose-a', 'nose-b', closed=True)
