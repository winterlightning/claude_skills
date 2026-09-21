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
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_bezier('heart-left-top', (24, 9), *(((21.5837553, 6.70714356), (17.27548816, 6), (13, 6)),))
        self.add_arc('heart-left', (13, 6), (6, 15), radius_x=11, radius_y=13, large_arc=False, sweep=False)
        self.add_bezier('heart-left-low', (6, 15), *(((6, 20.40784472), (6, 26.03394414), (8, 31)),))
        self.add_line('heart-tip-left', (8, 31), (24, 42))
        self.add_line('heart-tip-right', (24, 42), (40, 31))
        self.add_bezier('heart-right-low', (40, 31), *(((42, 26.03394414), (42, 20.40784472), (42, 15)),))
        self.add_arc('heart-right', (42, 15), (35, 6), radius_x=11, radius_y=13, large_arc=False, sweep=False)
        self.add_bezier('heart-right-top', (35, 6), *(((30.72451184, 6), (26.4162447, 6.70714356), (24, 9)),))
        self.add_arc('wing-upper-left', (24, 22), (15, 17), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_arc('wing-left', (15, 17), (17, 25), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_arc('wing-lower-left', (17, 25), (24, 27), radius_x=4, radius_y=2, large_arc=False, sweep=False)
        self.add_arc('wing-lower-right', (24, 27), (31, 25), radius_x=4, radius_y=2, large_arc=False, sweep=False)
        self.add_arc('wing-right', (31, 25), (33, 17), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_arc('wing-upper-right', (33, 17), (24, 22), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_contour('heart', *('heart-left-top', 'heart-left', 'heart-left-low', 'heart-tip-left', 'heart-tip-right', 'heart-right-low', 'heart-right', 'heart-right-top'), closed=True)
        self.add_contour('butterfly', *('wing-upper-left', 'wing-left', 'wing-lower-left', 'wing-lower-right', 'wing-right', 'wing-upper-right'), closed=True)
