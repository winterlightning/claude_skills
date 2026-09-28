"""Rounded rectangular camera body with a triangular right lens housing. Use four equal corner radii and split the right wall at the actual lens attachment."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '83306cac-34f4-4c2c-a7fe-6f53595d9c9c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__zoom-logo/20260927T082307Z-thuan-mac-1/reference/zoom logo_83306cac-34f4-4c2c-a7fe-6f53595d9c9c.svg'
AUTHOR = 'gpt-6'

class ZoomLogo(Solo48):
    icon_id = 'zoom-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('zoom', 'video-call', 'camera', 'meeting', 'logo', 'brand', 'conference')

    def build(self):
        # Plan: Rounded rectangular camera body with a triangular right lens housing. Use four equal corner radii and split the right wall at the actual lens attachment.
        # Exact keyshape ink extremes are owned by Keyshape.HRECT_L on SOLO48.

        self.add_line('top',(8,8),(28,8));self.add_arc('tr',(28,8),(32,12),radius_x=4)
        self.add_line('right-top',(32,12),(32,24));self.add_line('right-bottom',(32,24),(32,36));self.add_arc('br',(32,36),(28,40),radius_x=4)
        self.add_line('bottom',(28,40),(8,40));self.add_arc('bl',(8,40),(4,36),radius_x=4)
        self.add_line('left',(4,36),(4,12));self.add_arc('tl',(4,12),(8,8),radius_x=4)
        self.add_contour('body','top','tr','right-top','right-bottom','br','bottom','bl','left','tl',closed=True)
        self.add_polyline('lens',(32,24),(44,12),(44,36),closed=True);self.relate('connect','body','lens')

