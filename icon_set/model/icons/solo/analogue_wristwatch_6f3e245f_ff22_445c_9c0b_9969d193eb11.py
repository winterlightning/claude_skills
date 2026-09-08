"""An analogue wristwatch with an open strap, circular face and two hands; double bezel and crown omitted."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6f3e245f-ff22-445c-9c0b-9969d193eb11'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-01/watch_6f3e245f-ff22-445c-9c0b-9969d193eb11.svg'
AUTHOR = 'astra-chatgpt'


class AnalogueWristwatch(Solo48):
    icon_id = 'analogue-wristwatch'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('watch', 'wristwatch', 'time', 'clock', 'analogue', 'dial', 'strap', 'accessory')

    def build(self) -> None:
        # VRECT_L: authored directly to its SOLO48 centerline extremes.
        self.add_arc('face-a', (24, 8), (24, 40), radius_x=16, radius_y=16, sweep=True)
        self.add_arc('face-b', (24, 40), (24, 8), radius_x=16, radius_y=16, sweep=True)
        self.add_contour('face', 'face-a', 'face-b', closed=True)
        self.add_polyline('upper-strap', (24, 8), (16, 8), (16, 2), (32, 2), (32, 8), (24, 8), closed=False)
        self.add_polyline('lower-strap', (24, 40), (16, 40), (16, 46), (32, 46), (32, 40), (24, 40), closed=False)
        self.relate("connect", 'upper-strap', 'face')
        self.relate("connect", 'lower-strap', 'face')
        self.add_polyline('hands', (18, 20), (24, 24), (30, 19), closed=False)
