# Review candidate; original preserved.
"""An analogue wristwatch with taller open straps and a circular face. VRECT_M provides strap clearance; Lucide watch informs the shared strap and dial axis."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6f3e245f-ff22-445c-9c0b-9969d193eb11'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-01/watch_6f3e245f-ff22-445c-9c0b-9969d193eb11.svg'
AUTHOR = 'gpt-6'

class AnalogueWristwatchVariant4(Solo48):
    icon_id = 'analogue-wristwatch-v4'
    variant_of = 'analogue-wristwatch-v2'
    variant_label = 'Roomier openings — pending review'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('watch', 'wristwatch', 'time', 'clock', 'analogue', 'dial', 'strap', 'accessory')

    def build(self) -> None:
        """Opening repair: Extended both strap ends equally to enlarge their openings, preserving the dial and hands."""
        self.add_arc('face-top', (19, 12), (29, 12), radius_x=13)
        self.add_arc('face-right', (29, 12), (29, 36), radius_x=13)
        self.add_arc('face-bottom', (29, 36), (19, 36), radius_x=13)
        self.add_arc('face-left', (19, 36), (19, 12), radius_x=13)
        self.add_contour('face', 'face-top', 'face-right', 'face-bottom', 'face-left', closed=True)
        self.add_polyline('upper-strap', (19, 12), (19, 4), (29, 4), (29, 12))
        self.add_polyline('lower-strap', (19, 36), (19, 44), (29, 44), (29, 36))
        self.relate('connect', 'upper-strap', 'face')
        self.relate('connect', 'lower-strap', 'face')
        self.add_polyline('hands', (20, 21), (24, 24), (28, 20))
