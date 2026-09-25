"""Broad oval speech bubble with a lower-left tail and a concentric oval counter. Use smooth ellipse-like cubics and preserve the recognizable nested ring."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cd7bb35e-15fe-42c3-b3c6-4c5d1d93abcc'
SOURCE_PATH = 'pictographic-primitives/logos/technorati logo_cd7bb35e-15fe-42c3-b3c6-4c5d1d93abcc.svg'
AUTHOR = 'gpt-6'

class TechnoratiLogo(Solo48):
    icon_id = 'technorati-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('technorati', 'blog', 'search', 'speech-bubble', 'logo', 'brand', 'directory')

    def build(self):
        # Plan: Broad oval speech bubble with a lower-left tail and a concentric oval counter. Use smooth ellipse-like cubics and preserve the recognizable nested ring.
        # Exact keyshape ink extremes are owned by Keyshape.HRECT_L on SOLO48.

        self.add_bezier('bubble',(10,32),((6,29),(4,26),(4,22)),((4,14),(12,8),(24,8)),((36,8),(44,14),(44,22)),((44,30),(36,36),(24,36)),((22,36),(20,36),(18,35)))
        self.add_polyline('tail',(18,35),(8,40),(10,32))
        self.relate('connect','bubble','tail')
        self.add_arc('inner-top',(14,22),(34,22),radius_x=10,radius_y=5)
        self.add_arc('inner-bottom',(34,22),(14,22),radius_x=10,radius_y=5)
        self.add_contour('inner','inner-top','inner-bottom',closed=True)

