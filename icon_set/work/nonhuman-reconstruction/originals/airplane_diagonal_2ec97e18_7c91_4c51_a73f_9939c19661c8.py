"""Airplane. Keeps the upper-right nose, swept wings and tail fins; omits surface detail. Deliberate diagonal orientation.

SQUARE visible extremes (4, 4, 44, 44); centerlines (6, 6, 42, 42).
Lucide plane: one swept-wing silhouette with a rounded nose and distinct tail fins.
Mirrored subjects use paired coordinates; directional parts preserve their
intentional asymmetry. Geometry is authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2ec97e18-7c91-4c51-a73f-9939c19661c8'
SOURCE_PATH = 'pictographic-primitives/symbol/airplane_2ec97e18-7c91-4c51-a73f-9939c19661c8.svg'
AUTHOR = 'gpt-6'


class AirplaneDiagonal(Solo48):
    icon_id = 'airplane-diagonal'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/standalone"
    aliases = ()
    keywords = ('airplane', 'plane', 'flight', 'travel', 'aircraft', 'airport', 'trip', 'aviation')

    def build(self) -> None:
        self.add_arc('nose', (34, 6), (42, 14), radius_x=8, radius_y=8, sweep=True)
        self.add_line('outline-1', (42, 14), (34, 24))
        self.add_line('outline-2', (34, 24), (40, 36))
        self.add_line('outline-3', (40, 36), (36, 40))
        self.add_line('outline-4', (36, 40), (26, 30))
        self.add_line('outline-5', (26, 30), (20, 36))
        self.add_line('outline-6', (20, 36), (22, 42))
        self.add_line('outline-7', (22, 42), (16, 42))
        self.add_line('outline-8', (16, 42), (12, 34))
        self.add_line('outline-9', (12, 34), (6, 30))
        self.add_line('outline-10', (6, 30), (6, 24))
        self.add_line('outline-11', (6, 24), (14, 26))
        self.add_line('outline-12', (14, 26), (20, 20))
        self.add_line('outline-13', (20, 20), (8, 12))
        self.add_line('outline-14', (8, 12), (12, 8))
        self.add_line('outline-15', (12, 8), (26, 14))
        self.add_line('outline-16', (26, 14), (34, 6))
        self.add_contour('airframe', 'nose', 'outline-1', 'outline-2', 'outline-3', 'outline-4', 'outline-5', 'outline-6', 'outline-7', 'outline-8', 'outline-9', 'outline-10', 'outline-11', 'outline-12', 'outline-13', 'outline-14', 'outline-15', 'outline-16', closed=True)
