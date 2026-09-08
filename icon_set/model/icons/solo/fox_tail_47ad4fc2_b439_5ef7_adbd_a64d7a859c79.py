"""Seated fox with sharp ear and large curling brush tail; retain source asymmetry and omit crowded facial marks."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '47ad4fc2-b439-5ef7-adbd-a64d7a859c79'
SOURCE_PATH = 'pictographic-primitives/animals/fox tail_47ad4fc2-b439-5ef7-adbd-a64d7a859c79.svg'
AUTHOR = 'gpt-6'


class SittingFox(Solo48):
    icon_id = 'sitting-fox'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/animals"
    aliases = ()
    keywords = ('sitting', 'fox')

    def build(self) -> None:
        # Visible keyshape bounds: (3, 0, 45, 48); centerlines inset by 2.
        self.add_line('ear-back', (5, 19), (15, 2))
        self.add_line('ear-front', (15, 2), (15, 12))
        self.add_arc('brow', (15, 12), (24, 21), radius_x=9, radius_y=9, sweep=True)
        self.add_line('snout', (24, 21), (32, 21))
        self.add_arc('muzzle', (32, 21), (22, 29), radius_x=10, radius_y=8, sweep=True)
        self.add_arc('chest', (22, 29), (28, 38), radius_x=15, radius_y=15, sweep=False)
        self.add_arc('tail-inner', (28, 38), (38, 16), radius_x=23, radius_y=23, sweep=False)
        self.add_arc('tail-outer', (38, 16), (43, 30), radius_x=5, radius_y=14, sweep=True)
        self.add_arc('base-right', (43, 30), (27, 46), radius_x=16, radius_y=16, sweep=True)
        self.add_line('base', (27, 46), (10, 46))
        self.add_arc('base-left', (10, 46), (5, 41), radius_x=5, radius_y=5, sweep=True)
        self.add_line('back', (5, 41), (5, 19))
        self.add_contour('silhouette', 'ear-back', 'ear-front', 'brow', 'snout', 'muzzle', 'chest', 'tail-inner', 'tail-outer', 'base-right', 'base', 'base-left', 'back')
