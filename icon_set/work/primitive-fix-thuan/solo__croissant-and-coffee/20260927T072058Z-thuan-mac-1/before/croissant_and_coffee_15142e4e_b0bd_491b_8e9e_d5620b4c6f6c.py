"""Croissant and Coffee Cup. Retains the crescent and handled cup; uses two short pastry incisions instead of full partitions to avoid tiny closed pockets.

HRECT_L visible extremes (2, 6, 46, 42); centerlines (4, 8, 44, 40).
Lucide croissant: a curved pastry with a few large facets; Lucide coffee, inspected in batch 06, informed the rounded cup and handle.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '15142e4e-b0bd-491b-8e9e-d5620b4c6f6c'
SOURCE_PATH = 'pictographic-primitives/symbol/croissant_15142e4e-b0bd-491b-8e9e-d5620b4c6f6c.svg'
AUTHOR = 'gpt-6'


class CroissantAndCoffee(Solo48):
    icon_id = 'croissant-and-coffee'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol",)
    aliases = ()
    keywords = ('croissant', 'coffee', 'breakfast', 'bakery', 'cafe', 'pastry', 'food', 'morning')

    def build(self) -> None:
        self.add_line('cup-top-1', (14, 8), (28, 8))
        self.add_line('cup-top-2', (28, 8), (28, 16))
        self.add_arc('cup-se', (28, 16), (26, 18), radius_x=2, radius_y=2, sweep=True)
        self.add_line('cup-bottom', (26, 18), (16, 18))
        self.add_arc('cup-sw', (16, 18), (14, 16), radius_x=2, radius_y=2, sweep=True)
        self.add_line('cup-left', (14, 16), (14, 8))
        self.add_contour('cup', 'cup-top-1', 'cup-top-2', 'cup-se', 'cup-bottom', 'cup-sw', 'cup-left', closed=True)
        self.add_arc('handle', (28, 8), (28, 16), radius_x=8, radius_y=4, sweep=True)
        self.relate("connect", 'cup', 'handle')
        self.add_arc('outer-right', (44, 20), (36, 36), radius_x=20, radius_y=20, sweep=True)
        self.add_arc('outer-bottom', (36, 36), (12, 36), radius_x=20, radius_y=20, sweep=True)
        self.add_arc('outer-left', (12, 36), (4, 20), radius_x=20, radius_y=20, sweep=True)
        self.add_arc('inner-left', (4, 20), (12, 26), radius_x=20, radius_y=20, sweep=False)
        self.add_arc('inner-middle', (12, 26), (36, 26), radius_x=20, radius_y=10, sweep=False)
        self.add_arc('inner-right', (36, 26), (44, 20), radius_x=20, radius_y=20, sweep=False)
        self.add_contour('croissant', 'outer-right', 'outer-bottom', 'outer-left', 'inner-left', 'inner-middle', 'inner-right', closed=True)
        self.add_line('seam-left', (12, 36), (15, 35))
        self.add_line('seam-right', (36, 36), (33, 35))
        self.relate("connect", 'croissant', 'seam-left')
        self.relate("connect", 'croissant', 'seam-right')
