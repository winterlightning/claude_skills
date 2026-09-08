"""bird-in-flight: source silhouette re-authored on SOLO48.

Lucide bird informs coherent body arcs and sparse detail.
Keyshape HRECT_L; extremes obtained from the SOLO48 contract.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cc0d19d9-4136-5987-afa8-f2b8cb1ad36b'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird hunt_cc0d19d9-4136-5987-afa8-f2b8cb1ad36b.svg'
AUTHOR = 'gpt-6'


class BirdInFlight(Solo48):
    icon_id = 'bird-in-flight'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/birds"
    aliases = ()
    keywords = ('bird', 'flight', 'wings', 'hunting', 'swoop', 'sky', 'raptor', 'soar')

    def build(self) -> None:
        self.add_line('upper-left', (2, 8), (16, 11))
        self.add_arc('left-shoulder', (16, 11), (27, 26), radius_x=15, radius_y=15, sweep=True)
        self.add_arc('right-wing-front', (27, 26), (46, 8), radius_x=19, radius_y=18, sweep=True)
        self.add_line('right-wing-back', (46, 8), (36, 26))
        self.add_line('back', (36, 26), (38, 26))
        self.add_arc('head', (38, 26), (46, 34), radius_x=8, radius_y=8, sweep=True)
        self.add_line('beak', (46, 34), (37, 31))
        self.add_arc('breast', (37, 31), (25, 34), radius_x=16, radius_y=12, sweep=False)
        self.add_line('chest', (25, 34), (27, 40))
        self.add_line('belly', (27, 40), (19, 35))
        self.add_line('tail-top', (19, 35), (9, 40))
        self.add_arc('tail', (9, 40), (2, 33), radius_x=7, radius_y=7, sweep=True)
        self.add_line('tail-tip', (2, 33), (11, 30))
        self.add_line('underwing', (11, 30), (18, 24))
        self.add_arc('left-wing', (18, 24), (2, 8), radius_x=30, radius_y=30, sweep=True)
        self.add_contour('outline', 'upper-left', 'left-shoulder', 'right-wing-front', 'right-wing-back', 'back', 'head', 'beak', 'breast', 'chest', 'belly', 'tail-top', 'tail', 'tail-tip', 'underwing', 'left-wing', closed=True)
