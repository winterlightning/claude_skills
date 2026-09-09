"""Flying bird with raised wing, round head, short beak and broad tail. HRECT_L (2,8)-(46,40). Lucide bird informs a coherent body arc and clear beak; removed extra feather notches. Intentional flight-profile asymmetry."""
# Variant of bird-in-flight; parent file remains unchanged.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cc0d19d9-4136-5987-afa8-f2b8cb1ad36b'
SOURCE_PATH = 'pictographic-primitives/animals/wild bird hunt_cc0d19d9-4136-5987-afa8-f2b8cb1ad36b.svg'
AUTHOR = 'gpt-6'

class BirdInFlightVariant2(Solo48):
    icon_id = 'bird-in-flight-v2'
    variant_of = 'bird-in-flight'
    variant_label = 'Clear soaring bird silhouette'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals/birds'
    aliases = ()
    keywords = ('bird', 'flight', 'wings', 'hunting', 'swoop', 'sky', 'raptor', 'soar')

    def build(self) -> None:
        # Side-facing bird with raised wing, round head, beak and broad tail.
        # Centerline extremes (2,8)-(46,40); intentional flight asymmetry.
        self.add_line('wing-leading',(12,26),(18,8))
        self.add_arc('wing-round',(18,8),(29,23),radius_x=11,radius_y=15)
        self.add_arc('head',(29,23),(41,23),radius_x=6)
        self.add_line('beak-1', (41, 23), (46, 26))
        self.add_line('beak-2', (46, 26), (40, 29))
        self.add_arc('breast',(40,29),(25,40),radius_x=15,radius_y=11)
        self.add_line('belly',(25,40),(16,36))
        self.add_line('tail-1', (16, 36), (2, 39))
        self.add_line('tail-2', (2, 39), (8, 29))
        self.add_line('tail-3', (8, 29), (12, 26))
        self.add_contour('outline','wing-leading','wing-round','head','beak-1','beak-2','breast','belly','tail-1','tail-2','tail-3',closed=True)
