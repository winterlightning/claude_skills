# Variant of horse-head; parent file remains unchanged.
"""A left-facing horse head with a pricked ear and a single broad mane band."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c3f914af-7c9b-4941-8e99-c5be9d251a91'
SOURCE_PATH = 'pictographic-primitives/animals/zebra head_c3f914af-7c9b-4941-8e99-c5be9d251a91.svg'
AUTHOR = 'gpt-6'

class HorseHeadVariant2(Solo48):
    icon_id = 'horse-head-v2'
    variant_of = 'horse-head'
    variant_label = 'Design rules: exact bounds and open spacing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/animals'
    aliases = ('equine-head',)
    keywords = ('horse', 'head', 'profile', 'mane', 'equine', 'pony', 'zebra')

    def build(self):
        # Remove the secondary mane stripe: its enclosed wedge fails the hole gate.
        # Retain the equine outer mane, pricked ear, muzzle and eye.
        points = [(6, 28), (6, 26), (22, 12), (18, 8), (18, 6), (28, 8)]
        for j, (a, b) in enumerate(zip(points, points[1:]), 1):
            self.add_line(f'forehead-{j}', a, b)
        self.add_line('poll', (28, 8), (38, 12))
        self.add_arc('poll-back', (38, 12), (42, 20), radius_x=4, radius_y=8, sweep=True)
        self.add_arc('mane-back', (42, 20), (34, 42), radius_x=40, radius_y=40, sweep=True)
        self.add_line('neck-1', (34, 42), (29, 40))
        self.add_line('neck-mid', (29, 40), (24, 34))
        self.add_line('neck-2', (24, 34), (10, 36))
        self.add_arc('muzzle', (10, 36), (6, 28), radius_x=4, radius_y=8, sweep=True)
        self.add_contour('outline', *[f'forehead-{i}' for i in range(1, 6)], 'poll', 'poll-back', 'mane-back', 'neck-1', 'neck-mid', 'neck-2', 'muzzle', closed=True)

        self.add_dot('eye', (25, 21))
