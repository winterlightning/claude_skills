# Repair: Open the gap between the clasped thumb and the outer knuckles.
"""Two hands enter diagonally from opposite sides and clasp at the center. Overlapping thumbs cross the top of the grip, while curled fingers form a stepped row along the lower edge.
Lucide handshake overlapping thumb construction. Opposing diagonal wrists and clasped palms retained. Individual finger steps omitted; asymmetric thumb overlap retained.
SQUARE: centerline extremes (6,6)-(42,42); freshly authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '135d01ca-c11c-4e70-a645-04b5dbcd9502'
SOURCE_PATH = 'pictographic-primitives/work/workflow teamwork handshake_135d01ca-c11c-4e70-a645-04b5dbcd9502.svg'
AUTHOR = 'gpt-6'

class DiagonalHandshake(Solo48):
    icon_id = 'diagonal-handshake'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'work'
    aliases = ()
    keywords = ('hands', 'handshake', 'greeting', 'agreement', 'teamwork', 'grip')

    def build(self) -> None:
        self.add_polyline('outline', (6, 14), (14, 6), (22, 10), (28, 8), (42, 18), (36, 28), (26, 40), (22, 42), (6, 24), closed=True)
        self.add_line('thumb-start', (22, 10), (16, 16))
        self.add_arc('thumb-round', (16, 16), (22, 22), radius_x=5, radius_y=5, sweep=False, large_arc=False)
        self.add_polyline('thumb-end', (22, 22), (27, 18), (35, 27), (36, 28), closed=False)
        self.relate('connect', 'thumb-start', 'outline')
        self.relate('connect', 'thumb-start', 'thumb-round')
        self.relate('connect', 'thumb-round', 'thumb-end')
        self.relate('connect', 'thumb-end', 'outline')
