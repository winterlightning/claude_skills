"""Compass root owns a radius-20 face and a centrally symmetric diagonal diamond. Lucide compass informs the circle and isolated needle. Circle extrema (4,4)-(44,44).
Reduction: Removed the central needle divider to keep the diamond opening clear at 48px.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f5cf597c-471e-5d41-9ec4-382c9bc23bfa'
SOURCE_PATH = 'pictographic-primitives/navigation/compass direction_f5cf597c-471e-5d41-9ec4-382c9bc23bfa.svg'
AUTHOR = 'gpt-6'


class CompassDirection(Solo48):
    icon_id = 'compass-direction'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/navigation"
    aliases = ()
    keywords = ('compass', 'navigation', 'needle', 'direction', 'heading', 'orientation', 'travel')

    def build(self) -> None:
        center = 24
        face_radius = 20
        self.add_arc("face-top", (4, center), (44, center), radius_x=face_radius)
        self.add_arc("face-bottom", (44, center), (4, center), radius_x=face_radius)
        self.add_contour("face", "face-top", "face-bottom", closed=True)
        tip = (32, 16)
        shoulder = (28, 28)
        opposite = lambda p: (48-p[0], 48-p[1])
        self.add_polyline("needle", tip, shoulder, opposite(tip), opposite(shoulder), closed=True)
