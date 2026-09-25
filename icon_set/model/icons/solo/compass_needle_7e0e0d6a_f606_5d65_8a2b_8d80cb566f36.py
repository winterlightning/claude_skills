"""Compass root owns a radius-20 face and a centrally symmetric diagonal diamond. Lucide compass informs the circle and isolated needle. Circle extrema (4,4)-(44,44).
Reduction: Removed the central needle divider to keep the diamond opening clear at 48px.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7e0e0d6a-f606-5d65-8a2b-8d80cb566f36'
SOURCE_PATH = 'pictographic-primitives/navigation/compass_7e0e0d6a-f606-5d65-8a2b-8d80cb566f36.svg'
AUTHOR = 'gpt-6'


class Compass(Solo48):
    icon_id = 'compass-needle'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "navigation"
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
