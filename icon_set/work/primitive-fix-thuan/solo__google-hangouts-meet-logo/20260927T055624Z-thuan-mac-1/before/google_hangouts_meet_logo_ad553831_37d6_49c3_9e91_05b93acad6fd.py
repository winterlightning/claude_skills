"""A round speech bubble with a short tail at the bottom centre holds a video camera with a triangular lens housing at its right.

Plan: Radial bubble with directional tail; camera owns two lens attachment points with an 8-unit neck.
Keyshape: CIRCLE; exact SOLO48 envelope from the contract.
Construction reference: message-circle: continuous bubble outline.
Simplification: Small corner rounding omitted; wider circular envelope accommodates the lens.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ad553831-37d6-49c3-9e91-05b93acad6fd'
SOURCE_PATH = 'pictographic-primitives/logos/google hangouts meet logo_ad553831-37d6-49c3-9e91-05b93acad6fd.svg'
AUTHOR = 'gpt-6'


class GoogleHangoutsMeetLogo(Solo48):
    icon_id = 'google-hangouts-meet-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('google-meet', 'hangouts-meet', 'google', 'video-call', 'logo', 'brand', 'camera')

    def build(self):
        self.add_arc('bubble-top',(4,24),(44,24),radius_x=20)
        self.add_arc('bubble-right',(44,24),(36,40),radius_x=20)
        self.add_line('tail-1',(36,40),(24,44))
        self.add_line('tail-2',(24,44),(24,40))
        self.add_line('tail-3',(24,40),(12,40))
        self.add_arc('bubble-left',(12,40),(4,24),radius_x=20)
        self.add_contour('outline','bubble-top','bubble-right','tail-1','tail-2','tail-3','bubble-left',closed=True)
        self.add_polyline('camera',(14,18),(24,18),(24,20),(24,28),(24,30),(14,30),closed=True)
        self.add_polyline('lens',(24,20),(33,17),(33,31),(24,28))
        self.relate('connect','camera','lens')
