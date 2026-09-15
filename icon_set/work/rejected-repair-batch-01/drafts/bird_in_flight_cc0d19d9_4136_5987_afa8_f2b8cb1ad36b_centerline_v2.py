"""Smooth the raised wing into a broad tapered curve and give the belly a tangent return into the tail rather than a hard angular kink.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cc0d19d9-4136-5987-afa8-f2b8cb1ad36b'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird hunt_cc0d19d9-4136-5987-afa8-f2b8cb1ad36b.svg'
AUTHOR = 'gpt-6'

class BirdInFlight(Solo48):
    icon_id = 'bird-in-flight-centerline-v2'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals/birds'
    aliases = ()
    keywords = ('bird', 'flight', 'wings', 'hunting', 'swoop', 'sky', 'raptor', 'soar')

    def build(self) -> None:
        self.add_bezier('wing-leading', (12, 26), ((14, 20), (16, 12), (18, 8)))
        self.add_arc('wing-round', (18, 8), (29, 23), radius_x=11, radius_y=15)
        self.add_arc('head', (29, 23), (41, 23), radius_x=6)
        self.add_line('beak-1', (41, 23), (44, 26))
        self.add_line('beak-2', (44, 26), (40, 29))
        self.add_arc('breast', (40, 29), (25, 40), radius_x=15, radius_y=11)
        self.add_bezier('belly', (25, 40), ((22, 40), (19, 37), (16, 36)))
        self.add_line('tail-1', (16, 36), (4, 39))
        self.add_line('tail-2', (4, 39), (8, 29))
        self.add_line('tail-3', (8, 29), (12, 26))
        self.add_contour('outline', 'wing-leading', 'wing-round', 'head', 'beak-1', 'beak-2', 'breast', 'belly', 'tail-1', 'tail-2', 'tail-3', closed=True)
    variant_of = 'bird-in-flight'
    variant_label = 'Batch 01 centerline repair'
