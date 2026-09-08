"""Mirrored front-facing penguin and long crest plumes. Lucide bird informs broad curved contours. Chest seam and feet omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b013a26e-4b3d-4d2f-a975-ca81de5ad6ce'
SOURCE_PATH = 'pictographic-primitives/animals/penguin crested_b013a26e-4b3d-4d2f-a975-ca81de5ad6ce.svg'
AUTHOR = 'gpt-6'


class CrestedPenguin(Solo48):
    icon_id = 'crested-penguin'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ('rockhopper-penguin',)
    keywords = ('penguin', 'crest', 'bird', 'antarctic', 'flippers', 'rockhopper', 'standing', 'cold')

    def build(self) -> None:
        self.add_arc('body-1', (15, 8), (24, 5), radius_x=15, radius_y=15, sweep=True)
        self.add_arc('body-2', (24, 5), (33, 8), radius_x=15, radius_y=15, sweep=True)
        self.add_line('body-3', (33, 8), (36, 22))
        self.add_arc('body-4', (36, 22), (43, 32), radius_x=18, radius_y=18, sweep=True)
        self.add_line('body-5', (43, 32), (36, 29))
        self.add_line('body-6', (36, 29), (36, 36))
        self.add_arc('body-7', (36, 36), (24, 46), radius_x=12, radius_y=10, sweep=True)
        self.add_arc('body-8', (24, 46), (12, 36), radius_x=12, radius_y=10, sweep=True)
        self.add_line('body-9', (12, 36), (12, 29))
        self.add_line('body-10', (12, 29), (5, 32))
        self.add_arc('body-11', (5, 32), (12, 22), radius_x=18, radius_y=18, sweep=True)
        self.add_line('body-12', (12, 22), (15, 8))
        self.add_contour('body', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', 'body-8', 'body-9', 'body-10', 'body-11', 'body-12', closed=True)
        self.add_arc('crest-left-1', (15, 8), (5, 2), radius_x=14, radius_y=14, sweep=False)
        self.add_contour('crest-left', 'crest-left-1', closed=False)
        self.add_arc('crest-right-1', (33, 8), (43, 2), radius_x=14, radius_y=14, sweep=True)
        self.add_contour('crest-right', 'crest-right-1', closed=False)
        self.add_line('beak-1', (21, 25), (24, 29))
        self.add_line('beak-2', (24, 29), (27, 25))
        self.add_contour('beak', 'beak-1', 'beak-2', closed=False)
        self.add_dot('eye-left', (21, 17))
        self.add_dot('eye-right', (27, 17))
        self.relate("connect", 'body', 'crest-left')
        self.relate("connect", 'body', 'crest-right')
