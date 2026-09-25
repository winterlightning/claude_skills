"""A detached drop falls above a broad asymmetric puddle. HRECT extremes (4,8)-(44,40); puddle lobes share tangents.
Reduction: None.
Lucide construction: droplet
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '55d73bcc-348c-5d24-89f9-39afd521e3bc'
SOURCE_PATH = 'pictographic-primitives/nature/blood stain_55d73bcc-348c-5d24-89f9-39afd521e3bc.svg'
AUTHOR = 'gpt-6'


class DropFallingIntoPuddle(Solo48):
    icon_id = 'drop-falling-into-puddle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature"
    aliases = ()
    keywords = ('puddle', 'drop', 'stain', 'spill', 'liquid', 'blood', 'water', 'leak')

    def build(self) -> None:
        self.add_line("drop-top-1", (28,14), (34,8))
        self.add_line("drop-top-2", (34,8), (40,14))
        self.add_arc("drop-bottom",(40,14),(28,14),radius_x=6)
        self.add_contour("drop","drop-top-1","drop-top-2","drop-bottom",closed=True)
        self.add_arc("puddle-1",(4,34),(14,28),radius_x=10,radius_y=6)
        self.add_arc("puddle-2",(14,28),(24,32),radius_x=10,radius_y=4)
        self.add_line("puddle-3",(24,32),(34,32))
        self.add_arc("puddle-4",(34,32),(44,36),radius_x=10,radius_y=4)
        self.add_arc("puddle-5",(44,36),(34,40),radius_x=10,radius_y=4)
        self.add_line("puddle-6",(34,40),(14,40))
        self.add_arc("puddle-7",(14,40),(4,34),radius_x=10,radius_y=6)
        self.add_contour("puddle",*(f"puddle-{i}" for i in range(1,8)),closed=True)
