"""Corrected keyshape selection to match the existing square proportions.

SQUARE: visible ink (4, 4, 44, 44). Square envelope preserves the subject’s near-equal overall width and height.
Lucide bug: mirrored limb attachments around a rounded body.
"""
# Independent revision; parent models preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0b45fbf3-0b8c-5fad-b623-5d57b7e45c82'
SOURCE_PATH = 'pictographic-primitives/animals/robot spider_0b45fbf3-0b8c-5fad-b623-5d57b7e45c82.svg'
AUTHOR = 'gpt-6'

class SpiderWithRoundBodyVariant2(Solo48):
    icon_id = 'spider-with-round-body-v2'
    variant_of = 'spider-with-round-body'
    variant_label = 'Exact keyshape envelope and clear spacing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('spider', 'arachnid', 'legs', 'round', 'web', 'bug', 'halloween', 'insect')

    def build(self) -> None:
        self.add_arc('body-1', (24, 10), (32, 14), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('body-2', (32, 14), (34, 20), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('body-3', (34, 20), (32, 26), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('body-4', (32, 26), (24, 30), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('body-5', (24, 30), (16, 26), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('body-6', (16, 26), (14, 20), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('body-7', (14, 20), (16, 14), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('body-8', (16, 14), (24, 10), radius_x=10, radius_y=10, sweep=True)
        self.add_contour('body', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', 'body-8', closed=True)
        self.add_line('leg--1-0-1', (16, 14), (8, 6))
        self.add_line('leg--1-0-2', (8, 6), (6, 13))
        self.add_contour('leg--1-0', 'leg--1-0-1', 'leg--1-0-2', closed=False)
        self.relate('connect', 'body', 'leg--1-0')
        self.add_line('leg--1-1-1', (14, 20), (6, 21))
        self.add_line('leg--1-1-2', (6, 21), (6, 28))
        self.add_contour('leg--1-1', 'leg--1-1-1', 'leg--1-1-2', closed=False)
        self.relate('connect', 'body', 'leg--1-1')
        self.add_line('leg--1-2-1', (16, 26), (8, 31))
        self.add_line('leg--1-2-2', (8, 31), (6, 39))
        self.add_contour('leg--1-2', 'leg--1-2-1', 'leg--1-2-2', closed=False)
        self.relate('connect', 'body', 'leg--1-2')
        self.add_line('leg--1-3-1', (24, 30), (18, 36))
        self.add_line('leg--1-3-2', (18, 36), (16, 42))
        self.add_contour('leg--1-3', 'leg--1-3-1', 'leg--1-3-2', closed=False)
        self.relate('connect', 'body', 'leg--1-3')
        self.add_line('leg-1-0-1', (32, 14), (40, 6))
        self.add_line('leg-1-0-2', (40, 6), (42, 13))
        self.add_contour('leg-1-0', 'leg-1-0-1', 'leg-1-0-2', closed=False)
        self.relate('connect', 'body', 'leg-1-0')
        self.add_line('leg-1-1-1', (34, 20), (42, 21))
        self.add_line('leg-1-1-2', (42, 21), (42, 28))
        self.add_contour('leg-1-1', 'leg-1-1-1', 'leg-1-1-2', closed=False)
        self.relate('connect', 'body', 'leg-1-1')
        self.add_line('leg-1-2-1', (32, 26), (40, 31))
        self.add_line('leg-1-2-2', (40, 31), (42, 39))
        self.add_contour('leg-1-2', 'leg-1-2-1', 'leg-1-2-2', closed=False)
        self.relate('connect', 'body', 'leg-1-2')
        self.add_line('leg-1-3-1', (24, 30), (30, 36))
        self.add_line('leg-1-3-2', (30, 36), (32, 42))
        self.add_contour('leg-1-3', 'leg-1-3-1', 'leg-1-3-2', closed=False)
        self.relate('connect', 'body', 'leg-1-3')
        self.relate('connect', 'leg--1-3', 'leg-1-3')
