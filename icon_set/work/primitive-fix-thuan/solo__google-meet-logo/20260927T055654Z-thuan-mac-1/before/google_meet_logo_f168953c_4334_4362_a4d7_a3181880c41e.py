"""A video camera with a rectangular body, a notched upper left corner and a triangular lens housing at its right. A smaller rectangle sits inside the body.

Plan: Notched camera body owns both lens nodes and left-attached rectangular inset.
Keyshape: HRECT_L; exact SOLO48 envelope from the contract.
Construction reference: video: body and attached tapered lens.
Simplification: Small corner rounding omitted; notch and inset retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f168953c-4334-4362-a4d7-a3181880c41e'
SOURCE_PATH = 'pictographic-primitives/logos/google meet logo_f168953c-4334-4362-a4d7-a3181880c41e.svg'
AUTHOR = 'gpt-6'


class GoogleMeetLogo(Solo48):
    icon_id = 'google-meet-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('google-meet', 'google', 'video-call', 'camera', 'logo', 'brand', 'meeting')

    def build(self):
        self.add_polyline('body',(4,14),(10,8),(30,8),(30,16),(30,32),(30,40),(4,40),(4,30),(4,18),closed=True)
        self.add_polyline('lens',(30,16),(44,10),(44,38),(30,32))
        self.add_polyline('inset',(4,18),(20,18),(20,30),(4,30))
        self.relate('connect','body','lens')
        self.relate('connect','body','inset')
