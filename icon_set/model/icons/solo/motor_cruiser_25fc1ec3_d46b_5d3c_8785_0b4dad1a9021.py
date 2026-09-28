"""Motor Cruiser, rebuilt from the supplied reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '25fc1ec3-d46b-5d3c-8785-0b4dad1a9021'
SOURCE_PATH = 'pictographic-primitives/transportation/cruiser_25fc1ec3-d46b-5d3c-8785-0b4dad1a9021.svg'
AUTHOR = 'gpt-6'

class MotorCruiser(Solo48):
    icon_id = 'motor-cruiser'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    categories = ("transportation", "primitives")
    aliases = ()
    keywords = ('cruiser', 'motor yacht', 'boat', 'ship', 'ferry', 'marine', 'nautical', 'side view')

    def build(self) -> None:
        # HRECT_L: current contract centerline extremes (6, 8)-(42, 40).
        self.add_polyline('hull',(4,28),(12,28),(30,28),(36,24),(44,24),(40,34),(34,40),(10,40),closed=True)
        self.add_polyline('cabin',(12,28),(16,18),(20,18),(28,18),(32,18),(36,24))
        self.add_polyline('flybridge',(20,18),(20,8),(28,8),(28,18))
        self.relate('connect','hull','cabin')
        self.relate('connect','cabin','flybridge')
