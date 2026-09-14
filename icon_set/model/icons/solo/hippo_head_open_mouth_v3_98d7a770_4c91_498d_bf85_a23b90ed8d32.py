"""Corrected keyshape selection to match the existing square proportions.

SQUARE: visible ink (4, 4, 44, 44). Square envelope preserves the subject’s near-equal overall width and height.
No useful exact local Lucide match; retained the inspected parent silhouette.
"""
# Independent revision; parent models preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '98d7a770-4c91-498d-bf85-a23b90ed8d32'
SOURCE_PATH = 'pictographic-primitives/animals/hippo head side_98d7a770-4c91-498d-bf85-a23b90ed8d32.svg'
AUTHOR = 'gpt-6'

class HippoHeadOpenMouthVariant3(Solo48):
    icon_id = 'hippo-head-open-mouth-v3'
    variant_of = 'hippo-head-open-mouth-v2'
    variant_label = 'Exact keyshape envelope and clear spacing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('hippo', 'hippopotamus', 'head', 'mouth', 'open', 'jaw', 'profile', 'animal')

    def build(self) -> None:
        self.add_line('head-1', (6, 33), (11, 22))
        self.add_line('head-2', (11, 22), (10, 22))
        self.add_arc('head-3', (10, 22), (7, 19), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('head-4', (7, 19), (10, 16), radius_x=3, radius_y=3, sweep=True)
        self.add_line('head-5', (10, 16), (14, 17))
        self.add_line('head-6', (14, 17), (26, 6))
        self.add_line('head-7', (26, 6), (32, 6))
        self.add_line('head-8', (32, 6), (39, 11))
        self.add_line('head-9', (39, 11), (29, 21))
        self.add_arc('head-10', (29, 21), (27, 27), radius_x=10, radius_y=10, sweep=False)
        self.add_arc('head-11', (27, 27), (34, 32), radius_x=8, sweep=False)
        self.add_line('head-12', (34, 32), (42, 32))
        self.add_line('head-13', (42, 32), (42, 27))
        self.add_contour('head', *[f'head-{i}' for i in range(6, 14)])
        self.add_arc('lower-jaw-1', (42, 32), (35, 42), radius_x=11)
        self.add_line('lower-jaw-2', (35, 42), (22, 42))
        self.add_contour('lower-jaw', 'lower-jaw-1', 'lower-jaw-2')
        self.relate('connect', 'head', 'lower-jaw')
