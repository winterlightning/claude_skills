"""Dog Head Profile. Preserves the abstract left-facing profile, tall ear and long diagonal back; no facial details are added.

SQUARE visible extremes (4, 4, 44, 44); centerlines (6, 6, 42, 42).
Supplied reference; no useful exact Lucide match found.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '74ca938d-9d85-4544-b27a-8891d60149ba'
SOURCE_PATH = 'pictographic-primitives/symbol/dog head 1_74ca938d-9d85-4544-b27a-8891d60149ba.svg'
AUTHOR = 'gpt-6'


class DogHeadProfile(Solo48):
    icon_id = 'dog-head-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/standalone"
    aliases = ()
    keywords = ('dog', 'head', 'profile', 'pet', 'animal', 'canine', 'puppy', 'silhouette')

    def build(self) -> None:
        self.add_line('back-1', (42, 36), (28, 6))
        self.add_line('back-2', (28, 6), (24, 16))
        self.add_arc('forehead', (24, 16), (20, 18), radius_x=4, radius_y=4, sweep=True)
        self.add_line('snout-top', (20, 18), (14, 18))
        self.add_arc('snout', (14, 18), (14, 32), radius_x=8, radius_y=7, sweep=False)
        self.add_line('neck-1', (14, 32), (24, 34))
        self.add_line('neck-2', (24, 34), (26, 42))
        self.add_contour('profile', 'back-1', 'back-2', 'forehead', 'snout-top', 'snout', 'neck-1', 'neck-2')
