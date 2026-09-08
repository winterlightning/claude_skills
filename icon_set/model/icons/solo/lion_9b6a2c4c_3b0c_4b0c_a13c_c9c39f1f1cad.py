"""A fixed butterfly-and-heart emblem. Lucide heart informs paired rounded lobes and smooth shoulders. Butterfly wing veins and antennae omitted; all geometry mirrored about x=24."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9b6a2c4c-3b0c-4b0c-a13c-c9c39f1f1cad'
SOURCE_PATH = 'pictographic-primitives/animals/lion_9b6a2c4c-3b0c-4b0c-a13c-c9c39f1f1cad.svg'
AUTHOR = 'gpt-6'


class ButterflyInHeart(Solo48):
    icon_id = 'butterfly-in-heart'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('butterfly', 'in', 'heart', 'animal')

    def build(self) -> None:
        # SQUARE: authored to its exact SOLO48 centerline bounds.
        self.add_arc('heart-left-top', (24, 9), (13, 2), radius_x=11, radius_y=7, sweep=False)
        self.add_arc('heart-left', (13, 2), (2, 15), radius_x=11, radius_y=13, sweep=False)
        self.add_arc('heart-left-low', (2, 15), (8, 31), radius_x=25, radius_y=25, sweep=False)
        self.add_line('heart-tip-left', (8, 31), (24, 46))
        self.add_line('heart-tip-right', (24, 46), (40, 31))
        self.add_arc('heart-right-low', (40, 31), (46, 15), radius_x=25, radius_y=25, sweep=False)
        self.add_arc('heart-right', (46, 15), (35, 2), radius_x=11, radius_y=13, sweep=False)
        self.add_arc('heart-right-top', (35, 2), (24, 9), radius_x=11, radius_y=7, sweep=False)
        self.add_contour('heart', 'heart-left-top', 'heart-left', 'heart-left-low', 'heart-tip-left', 'heart-tip-right', 'heart-right-low', 'heart-right', 'heart-right-top', closed=True)
        self.add_arc('wing-upper-left', (24, 23), (13, 17), radius_x=7, radius_y=7, sweep=False)
        self.add_arc('wing-left', (13, 17), (15, 27), radius_x=7, radius_y=7, sweep=False)
        self.add_arc('wing-lower-left', (15, 27), (24, 29), radius_x=5, radius_y=3, sweep=False)
        self.add_arc('wing-lower-right', (24, 29), (33, 27), radius_x=5, radius_y=3, sweep=False)
        self.add_arc('wing-right', (33, 27), (35, 17), radius_x=7, radius_y=7, sweep=False)
        self.add_arc('wing-upper-right', (35, 17), (24, 23), radius_x=7, radius_y=7, sweep=False)
        self.add_contour('butterfly', 'wing-upper-left', 'wing-left', 'wing-lower-left', 'wing-lower-right', 'wing-right', 'wing-upper-right', closed=True)
