"""camera-8b077ef0 — re-authored in place for smooth SOLO48 geometry."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8b077ef0-ba0d-405b-8332-a61869ec5707'
SOURCE_PATH = 'pictographic-primitives/photography/camera_8b077ef0-ba0d-405b-8332-a61869ec5707.svg'
AUTHOR = 'gpt-6'

class Camera8b077ef0(Solo48):
    icon_id = 'camera-8b077ef0'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'photography'
    categories = ('photography', 'primitives')
    aliases = ()
    keywords = ('camera', 'photography')

    def build(self):
        # Symmetric camera shell: shared four-unit corner radius, raised prism.
        # Lucide camera informs matching tangent corners and the circular lens.
        # HRECT_L extremes: (4,8)-(44,40). Lens restores camera recognition.
        prism = [(14,14), (18,8), (30,8), (34,14), (40,14)]
        for i, (start, end) in enumerate(zip(prism, prism[1:]), 1):
            self.add_line(f'prism-{i}', start, end)
        self.add_arc('top-right', (40,14), (44,18), radius_x=4)
        self.add_line('right', (44,18), (44,36))
        self.add_arc('bottom-right', (44,36), (40,40), radius_x=4)
        self.add_line('bottom', (40,40), (8,40))
        self.add_arc('bottom-left', (8,40), (4,36), radius_x=4)
        self.add_line('left', (4,36), (4,18))
        self.add_arc('top-left', (4,18), (8,14), radius_x=4)
        self.add_line('shoulder-left', (8,14), (14,14))
        self.add_contour('outline', 'prism-1', 'prism-2', 'prism-3', 'prism-4', 'top-right', 'right', 'bottom-right', 'bottom', 'bottom-left', 'left', 'top-left', 'shoulder-left', closed=True)
        self.add_arc('lens-top', (19,26), (29,26), radius_x=5)
        self.add_arc('lens-bottom', (29,26), (19,26), radius_x=5)
        self.add_contour('lens', 'lens-top', 'lens-bottom', closed=True)
