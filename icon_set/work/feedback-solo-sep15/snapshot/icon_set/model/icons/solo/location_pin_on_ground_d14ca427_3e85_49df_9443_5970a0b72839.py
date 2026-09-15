"""A teardrop location pin points into a ground ring. Lucide map-pin informs the circular head and tapered foot. Keep the foreground half of the ground ellipse; remove its occluded rear half and inner ring to leave clearance. Mirrored about x=24."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd14ca427-3e85-49df-9443-5970a0b72839'
SOURCE_PATH = 'pictographic-primitives/protection/surveillance location_d14ca427-3e85-49df-9443-5970a0b72839.svg'
AUTHOR = 'gpt-6'


class ProtectionIcon(Solo48):
    icon_id = 'location-pin-on-ground'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/protection"
    aliases = ()
    keywords = ('location', 'pin', 'map', 'marker', 'place', 'tracking', 'surveillance', 'gps')

    def build(self):
        # SQUARE centerline extremes (6, 6, 42, 42).

        # Pin owns its hole; a detached foreground half-ellipse marks the ground.
        self.add_arc('pin-top',(12,18),(36,18),radius_x=12)
        self.add_arc('pin-right',(36,18),(24,33),radius_x=16)
        self.add_arc('pin-left',(24,33),(12,18),radius_x=16)
        self.add_contour('pin','pin-top','pin-right','pin-left',closed=True)
        self.add_arc('hole-top',(21,18),(27,18),radius_x=3)
        self.add_arc('hole-bottom',(27,18),(21,18),radius_x=3)
        self.add_contour('hole','hole-top','hole-bottom',closed=True)
        self.add_arc('ground',(42,34),(6,34),radius_x=18,radius_y=8)
